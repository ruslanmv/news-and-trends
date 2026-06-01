#!/usr/bin/env python3
"""
test_trends.py — unit tests for the trend text parsing / validation layer.

Dependency-free (stdlib ``unittest`` only) so it runs in any environment without
the heavy crewai / sklearn stack. Exercises every malformed LLM-output shape
observed in production plus the repair tool and the CI safety gate.

Run directly:  python scripts/test_trends.py
Or via Make:    make test
"""
import os
import sys
import unittest
from glob import glob

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import trend_text as tt
import repair_trends as rt

ISSUES_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site", "issues"
)


def _no_wrapper(text: str) -> bool:
    return not any(s in text for s in ('"""', "'''")) and not text.lstrip().startswith("{") \
        and '"body":' not in text and '"title":' not in text


class TestRecovery(unittest.TestCase):
    """recover_title_and_body across every shape the LLM actually emits."""

    def test_plain_escaped_json(self):
        t, b = tt.recover_title_and_body(
            '{"title": "T One", "body": "Line one.\\n\\nLine two with \\"q\\"."}'
        )
        self.assertEqual(t, "T One")
        self.assertEqual(b, 'Line one.\n\nLine two with "q".')

    def test_triple_quoted_closed_dict(self):
        t, b = tt.recover_title_and_body('{ "title": "T2", "body": """# H\n\nBody.\n""" }')
        self.assertEqual(t, "T2")
        self.assertIn("# H", b)
        self.assertTrue(_no_wrapper(b))

    def test_triple_quoted_unterminated(self):
        # The exact trend-2026-06-01 failure: no closing """ or }.
        blob = '{\n  "title": "Meta\'s AI Domination",\n  "body": """\n## Analysis\n\nMeta leads.\n'
        t, b = tt.recover_title_and_body(blob)
        self.assertEqual(t, "Meta's AI Domination")
        self.assertTrue(b.startswith("## Analysis"))
        self.assertTrue(_no_wrapper(b))

    def test_single_triple_quote(self):
        t, b = tt.recover_title_and_body("{ 'title': 'T3', 'body': '''# Yo\n\ntext''' }")
        self.assertEqual(t, "T3")
        self.assertEqual(b, "# Yo\n\ntext")

    def test_unterminated_plain_string_with_newlines(self):
        # The trend-2026-05-02 family: normal quote opens, literal newlines, no close.
        blob = '{\n  "title": "T4",\n  "body": "## Heading ##\n\nProse paragraph here.'
        t, b = tt.recover_title_and_body(blob)
        self.assertEqual(t, "T4")
        self.assertIn("Heading", b)
        self.assertTrue(_no_wrapper(b))

    def test_markdown_fenced(self):
        blob = '```json\n{"title": "T5", "body": "Hello world."}\n```'
        t, b = tt.recover_title_and_body(blob)
        self.assertEqual(t, "T5")
        self.assertEqual(b, "Hello world.")


class TestParseTrendOutput(unittest.TestCase):
    """parse_trend_output — the Markdown-first, model-agnostic entry point."""

    def test_markdown_with_heading(self):
        md = "## The Rise of Agentic AI\n\n### Current Landscape\n\nAgents are everywhere."
        t, b = tt.parse_trend_output(md, fallback_title="FB")
        self.assertEqual(t, "The Rise of Agentic AI")
        self.assertTrue(b.startswith("### Current Landscape"))  # leading title stripped
        self.assertNotIn("## The Rise", b)

    def test_markdown_without_heading_uses_fallback(self):
        md = "Agents are becoming the dominant pattern in AI this week."
        t, b = tt.parse_trend_output(md, fallback_title="Google: Agents Lead")
        self.assertEqual(t, "Google: Agents Lead")
        self.assertEqual(b, md)

    def test_fenced_markdown_is_unwrapped(self):
        md = "```markdown\n## Quantum Leap\n\nBody text.\n```"
        t, b = tt.parse_trend_output(md, fallback_title="FB")
        self.assertEqual(t, "Quantum Leap")
        self.assertEqual(b, "Body text.")

    def test_json_response_still_recovered(self):
        # A model that ignores the Markdown instruction and returns JSON.
        blob = '{ "title": "JSON Title", "body": """\n## H\n\nProse.\n""" }'
        t, b = tt.parse_trend_output(blob, fallback_title="FB")
        self.assertEqual(t, "JSON Title")
        self.assertIn("## H", b)
        self.assertTrue(_no_wrapper(b))

    def test_malformed_json_does_not_leak_wrapper(self):
        blob = '{"title": "T", "body": "## Heading ##\n\nUnterminated prose...'
        t, b = tt.parse_trend_output(blob, fallback_title="FB")
        self.assertTrue(_no_wrapper(b))
        self.assertIn("Heading", b)


class TestValidateGuard(unittest.TestCase):
    """validate_trend_body — the pre-write safety net."""

    def test_clean_passthrough(self):
        clean = "## Real Heading\n\nThis is clean prose."
        self.assertEqual(tt.validate_trend_body(clean), clean)

    def test_sanitises_wrapper(self):
        out = tt.validate_trend_body('{ "title": "X", "body": """\n## H\n\nText.\n"""')
        self.assertIn("## H", out)
        self.assertTrue(_no_wrapper(out))

    def test_placeholder_for_unsalvageable(self):
        out = tt.validate_trend_body('{ broken "title": leftover fragment')
        self.assertEqual(out, tt.SAFE_PLACEHOLDER_BODY)

    def test_is_unsafe_body(self):
        self.assertTrue(tt.is_unsafe_body('{ "title": "x"'))
        self.assertTrue(tt.is_unsafe_body('text "body": more'))
        self.assertFalse(tt.is_unsafe_body("## Clean\n\nbody"))


class TestRepairBody(unittest.TestCase):
    """repair_trends.repair_body region handling."""

    def test_repairs_json_region(self):
        region = '{\n  "title": "Good Title",\n  "body": "## Body\n\nText."'
        body, title = rt.repair_body(region)
        self.assertEqual(title, "Good Title")
        self.assertTrue(body.startswith("## Body"))

    def test_clean_region_untouched(self):
        self.assertEqual(rt.repair_body("## Already clean\n\nProse."), (None, None))


class TestPublishedContentGate(unittest.TestCase):
    """Integration: every committed trend file must already be clean."""

    def test_all_published_files_clean(self):
        files = sorted(glob(os.path.join(ISSUES_DIR, "trend-*.md")))
        self.assertGreater(len(files), 0, "no trend files found to validate")
        self.assertEqual(rt.check_files(files), 0, "published trend files contain raw wrappers")


if __name__ == "__main__":
    unittest.main(verbosity=2)
