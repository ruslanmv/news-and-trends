#!/usr/bin/env python3
"""
generate_featured_trend.py — optional standalone generator for the homepage
"Featured Trend" feed.

In production this feed is produced by the Eleventy template
``site/featured-trend.njk`` during ``npm run build`` and served at
``/news-and-trends/featured-trend.json``. This script reproduces the *same*
JSON from the latest trend post in ``site/issues/`` WITHOUT needing a full
Eleventy build (or the LLM pipeline), so you can quickly (re)generate and test
it — e.g. to confirm the ruslanmv.com homepage "Featured Trend" card will pick
up new content.

Usage:
    python scripts/generate_featured_trend.py                 # write site/docs/featured-trend.json
    python scripts/generate_featured_trend.py --print         # also print the JSON
    python scripts/generate_featured_trend.py -o some/path.json
    python scripts/generate_featured_trend.py --check         # print only, don't write (CI/test)

Pure standard library — no dependencies.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ISSUES_DIR = os.path.join(BASE_DIR, "site", "issues")
DEFAULT_OUT = os.path.join(BASE_DIR, "site", "docs", "featured-trend.json")
PATH_PREFIX = "/news-and-trends"          # matches site/.eleventy.js pathPrefix
SECTION_URL = "/news-and-trends/"
SUMMARY_LEN = 220                         # matches the njk `truncate(220)`

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.S)


def parse_front_matter(text: str):
    """Return (front_matter_dict, body). Minimal YAML — flat scalars only."""
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    head, body = m.group(1), m.group(2)
    data = {}
    for line in head.splitlines():
        m2 = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if m2 and m2.group(2).strip():
            data[m2.group(1)] = m2.group(2).strip().strip("\"'")
    return data, body


def parse_date(value: str):
    try:
        return datetime.strptime(str(value).strip().strip("\"'")[:10], "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def readable_date(d) -> str:
    """en-US long date, e.g. 'June 4, 2026' (matches the njk readableDate filter)."""
    return "{month} {day}, {year}".format(month=d.strftime("%B"), day=d.day, year=d.year) if d else ""


def to_summary(body: str, length: int = SUMMARY_LEN) -> str:
    """Approximate Eleventy's `content | striptags | truncate(length)`:
    strip the Markdown to text, keep paragraph breaks, cut to `length` + '...'."""
    body = re.split(r"\n-{3,}\s*\n", body)[0]          # drop the appended Methodology block
    lines = []
    for ln in body.splitlines():
        s = ln.strip()
        if not s:
            continue
        s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)      # images
        s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)  # links -> text
        s = re.sub(r"[*_`#>]+", "", s)                  # emphasis / headings / quotes
        s = re.sub(r"^[-+]\s+", "", s)                  # list bullets
        s = re.sub(r"[ \t]+", " ", s).strip()
        if s:
            lines.append(s)
    text = "\n".join(lines)
    if len(text) > length:
        text = text[:length] + "..."
    return text


def latest_trend_file():
    files = glob.glob(os.path.join(ISSUES_DIR, "trend-*.md"))
    if not files:
        return None
    # Newest first by front-matter date, then by filename (mirrors collections.trend | first)
    def key(path):
        with open(path, "r", encoding="utf-8") as f:
            fm, _ = parse_front_matter(f.read())
        d = parse_date(fm.get("date", "")) or parse_date(
            os.path.basename(path).replace("trend-", "").replace(".md", "")
        )
        return (d.toordinal() if d else 0, os.path.basename(path))
    return sorted(files, key=key, reverse=True)[0]


def build_feed():
    path = latest_trend_file()
    if not path:
        # Same fallback the njk template emits when there are no trends yet.
        return {
            "title": "AI Trends & Analysis",
            "summary": "The latest AI and technology trend analysis, refreshed every day.",
            "date": "",
            "label": "Trend Analysis",
            "url": SECTION_URL,
            "section_url": SECTION_URL,
        }
    with open(path, "r", encoding="utf-8") as f:
        fm, body = parse_front_matter(f.read())
    slug = os.path.splitext(os.path.basename(path))[0]      # e.g. trend-2026-06-04
    return {
        "title": fm.get("title", "AI Trends & Analysis"),
        "summary": to_summary(body),
        "date": readable_date(parse_date(fm.get("date", ""))),
        "label": "Trend Analysis",
        "url": "{prefix}/issues/{slug}/".format(prefix=PATH_PREFIX, slug=slug),
        "section_url": SECTION_URL,
    }


def main():
    ap = argparse.ArgumentParser(description="Generate the homepage Featured Trend feed.")
    ap.add_argument("-o", "--out", default=DEFAULT_OUT, help="output path (default: site/docs/featured-trend.json)")
    ap.add_argument("--print", dest="show", action="store_true", help="print the JSON to stdout")
    ap.add_argument("--check", action="store_true", help="print only, do not write a file")
    args = ap.parse_args()

    feed = build_feed()
    payload = json.dumps(feed, ensure_ascii=False, indent=2)

    if args.check:
        print(payload)
        return

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(payload + "\n")
    print("✅ Wrote {0} ({1})".format(os.path.relpath(args.out, BASE_DIR), feed["url"]))
    if args.show:
        print(payload)


if __name__ == "__main__":
    main()
