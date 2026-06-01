#!/usr/bin/env python3
"""
repair_trends.py

One-off maintenance utility that cleans legacy trend files whose body was
written as a raw, often-unterminated JSON blob (e.g. `{ "title": ..., "body": ... }`)
instead of plain Markdown. This happened when the LLM response could not be
parsed and the whole response was dumped verbatim as the body.

For every `site/issues/trend-*.md` whose body region looks like JSON, this:
  1. Extracts the `body` value (un-escaping \\n, \\", etc.) -> clean Markdown.
  2. Extracts the `title` value and uses it to replace the generic fallback
     title in the front matter ("AI Technology Trends: What's Emerging This Week").
  3. Rewrites the file, preserving the front matter and the Methodology footer.

Handles every malformed shape observed in practice:
  * standard escaped JSON strings,
  * Python-style triple-quoted bodies (``"body": \"\"\" ... \"\"\"``), and
  * unterminated strings (missing closing quote / brace from truncated output).

Idempotent: files whose body is already plain Markdown are left untouched.

Usage:
    python scripts/repair_trends.py            # repair in place
    python scripts/repair_trends.py --dry-run  # report only
    python scripts/repair_trends.py --check    # CI gate: exit 1 if any wrapper remains
"""

import argparse
import os
import re
import sys
from glob import glob

from trend_text import UNSAFE_BODY_PATTERNS, extract_field

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ISSUES_DIR = os.path.join(BASE_DIR, "site", "issues")

GENERIC_TITLE = "AI Technology Trends: What's Emerging This Week"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def repair_body(body_region: str):
    """Return (new_body_markdown, extracted_title) if the region is a JSON blob, else (None, None).

    Parsing of the malformed wrapper (standard JSON, Python triple-quoted, and
    unterminated values) is delegated to :mod:`trend_text`, the single source of
    truth shared with the generator.
    """
    stripped = body_region.strip()
    if not stripped.startswith("{") or '"body"' not in stripped:
        return None, None
    body = extract_field(stripped, "body")
    if not body:
        return None, None
    title = extract_field(stripped, "title")
    return body.strip(), (title.strip() or None)


def process_file(path: str, dry_run: bool = False) -> bool:
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    m = FRONTMATTER_RE.match(raw)
    if not m:
        return False
    frontmatter, rest = m.group(1), m.group(2)

    # Split off the Methodology footer so we only touch the analysis body.
    idx = rest.find("## Methodology")
    if idx != -1:
        body_region = rest[:idx].rstrip().rstrip("-").rstrip()
        footer = rest[idx:]
    else:
        body_region = rest.rstrip()
        footer = ""

    new_body, new_title = repair_body(body_region)
    if new_body is None:
        return False  # already clean

    if new_title:
        # Replace generic / existing title in front matter with the real one.
        safe = new_title.replace('"', "'")
        if re.search(r'^title:\s*.*$', frontmatter, flags=re.MULTILINE):
            frontmatter = re.sub(r'^title:\s*.*$', f'title: "{safe}"', frontmatter, count=1, flags=re.MULTILINE)

    footer_block = ("\n\n---\n\n" + footer) if footer else "\n"
    new_content = f"---\n{frontmatter}\n---\n\n{new_body}{footer_block}"

    if dry_run:
        print(f"[would repair] {os.path.basename(path)}"
              + (f"  ->  {new_title}" if new_title else ""))
        return True

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"[repaired] {os.path.basename(path)}" + (f"  ->  {new_title}" if new_title else ""))
    return True


def check_files(files) -> int:
    """CI gate: exit non-zero if any published trend file still contains a raw
    LLM wrapper artifact in its body. Front matter is excluded from the scan.
    Uses the same wrapper signatures the generator validates against."""
    bad = []
    for path in files:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
        m = FRONTMATTER_RE.match(raw)
        body = m.group(2) if m else raw
        hits = [p for p in UNSAFE_BODY_PATTERNS if re.search(p, body, re.DOTALL)]
        if hits:
            bad.append((os.path.basename(path), hits))

    if bad:
        print("❌ Unsafe wrapper artifacts found in generated trend files:")
        for name, hits in bad:
            print(f"   - {name}: {', '.join(hits)}")
        print(f"\n{len(bad)} / {len(files)} trend files are unsafe to publish.")
        return 1
    print(f"✅ All {len(files)} trend files are clean (no raw JSON/dict wrappers).")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Repair / validate trend Markdown files.")
    ap.add_argument("--dry-run", action="store_true", help="Report changes without writing.")
    ap.add_argument("--check", action="store_true",
                    help="CI gate: exit 1 if any trend file still contains a raw wrapper.")
    args = ap.parse_args()

    files = sorted(glob(os.path.join(ISSUES_DIR, "trend-*.md")))
    if not files:
        print(f"No trend files found in {ISSUES_DIR}", file=sys.stderr)
        return 1

    if args.check:
        return check_files(files)

    repaired = sum(process_file(p, dry_run=args.dry_run) for p in files)
    print(f"\n{repaired} / {len(files)} trend files "
          f"{'would be ' if args.dry_run else ''}repaired.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
