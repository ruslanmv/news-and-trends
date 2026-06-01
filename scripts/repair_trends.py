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

Idempotent: files whose body is already plain Markdown are left untouched.

Usage:
    python scripts/repair_trends.py            # repair in place
    python scripts/repair_trends.py --dry-run  # report only
"""

import argparse
import os
import re
import sys
from glob import glob

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ISSUES_DIR = os.path.join(BASE_DIR, "site", "issues")

GENERIC_TITLE = "AI Technology Trends: What's Emerging This Week"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def _scan_json_string(text: str, start: int):
    """Scan a JSON double-quoted string beginning at `text[start] == '\"'`.

    Returns (decoded_value, index_after_closing_quote) or (None, start) on failure.
    Handles standard JSON escapes plus literal (unescaped) newlines, which the
    malformed blobs sometimes contain.
    """
    if start >= len(text) or text[start] != '"':
        return None, start
    i = start + 1
    out = []
    escapes = {'"': '"', "\\": "\\", "/": "/", "n": "\n", "t": "\t", "r": "\r", "b": "\b", "f": "\f"}
    while i < len(text):
        c = text[i]
        if c == "\\":
            if i + 1 < len(text):
                nxt = text[i + 1]
                if nxt == "u" and i + 5 < len(text):
                    try:
                        out.append(chr(int(text[i + 2:i + 6], 16)))
                        i += 6
                        continue
                    except ValueError:
                        pass
                out.append(escapes.get(nxt, nxt))
                i += 2
                continue
            out.append(c)
            i += 1
        elif c == '"':
            return "".join(out), i + 1
        else:
            out.append(c)
            i += 1
    return None, start  # unterminated


def _extract_field(blob: str, field: str):
    """Extract a top-level string field value from a (possibly malformed) JSON blob."""
    m = re.search(r'"' + re.escape(field) + r'"\s*:\s*', blob)
    if not m:
        return None
    return _scan_json_string(blob, m.end())[0]


def repair_body(body_region: str):
    """Return (new_body_markdown, extracted_title) if the region is a JSON blob, else (None, None)."""
    stripped = body_region.strip()
    if not stripped.startswith("{") or '"body"' not in stripped:
        return None, None
    body = _extract_field(stripped, "body")
    title = _extract_field(stripped, "title")
    if not body:
        return None, None
    return body.strip(), (title.strip() if title else None)


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


def main() -> int:
    ap = argparse.ArgumentParser(description="Repair legacy raw-JSON trend files.")
    ap.add_argument("--dry-run", action="store_true", help="Report changes without writing.")
    args = ap.parse_args()

    files = sorted(glob(os.path.join(ISSUES_DIR, "trend-*.md")))
    if not files:
        print(f"No trend files found in {ISSUES_DIR}", file=sys.stderr)
        return 1

    repaired = sum(process_file(p, dry_run=args.dry_run) for p in files)
    print(f"\n{repaired} / {len(files)} trend files "
          f"{'would be ' if args.dry_run else ''}repaired.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
