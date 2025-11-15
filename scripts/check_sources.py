#!/usr/bin/env python3
"""
check_sources.py

Simple health check for all RSS/Atom feeds defined in scripts/sources.json.

It will:
- Fetch each feed
- Report HTTP status (if available)
- Warn on parse errors
- Show how many entries were found

Exit code:
- 0 if all feeds are reachable and parseable
- 1 if at least one feed has a hard error
"""

import json
import os
import sys
import time
from typing import Any, Dict, List

import feedparser

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOURCES_FILE = os.path.join(BASE_DIR, "scripts", "sources.json")


def load_sources() -> List[Dict[str, Any]]:
    if not os.path.exists(SOURCES_FILE):
        raise FileNotFoundError(f"Sources file not found: {SOURCES_FILE}")
    with open(SOURCES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def check_source(source: Dict[str, Any]) -> Dict[str, Any]:
    name = source.get("name", "<unnamed>")
    url = source.get("url")
    if not url:
        return {
            "name": name,
            "url": url,
            "ok": False,
            "reason": "Missing URL",
            "status": None,
            "entries": 0,
            "duration": 0.0,
        }

    print(f"🔎 Checking: {name} — {url}")
    start = time.time()
    feed = feedparser.parse(url)
    duration = time.time() - start

    status = getattr(feed, "status", None)
    bozo = bool(getattr(feed, "bozo", 0))
    bozo_exception = getattr(feed, "bozo_exception", None)
    entries = len(feed.entries or [])

    ok = True
    reason = "OK"

    if status is not None and status >= 400:
        ok = False
        reason = f"HTTP {status}"
    elif bozo and entries == 0:
        ok = False
        reason = f"Parse error: {bozo_exception!r}"
    elif entries == 0:
        # Soft warning: reachable, but no items
        ok = True
        reason = "No entries (WARN)"

    return {
        "name": name,
        "url": url,
        "ok": ok,
        "reason": reason,
        "status": status,
        "entries": entries,
        "duration": duration,
    }


def main() -> None:
    print("======================================")
    print("  RSS SOURCES HEALTH CHECK            ")
    print("======================================\n")

    try:
        sources = load_sources()
    except Exception as e:
        print(f"❌ Failed to load sources.json: {e}")
        sys.exit(1)

    results: List[Dict[str, Any]] = []
    for src in sources:
        try:
            res = check_source(src)
        except Exception as e:
            res = {
                "name": src.get("name", "<unnamed>"),
                "url": src.get("url"),
                "ok": False,
                "reason": f"Exception: {e!r}",
                "status": None,
                "entries": 0,
                "duration": 0.0,
            }
        results.append(res)
        print(f"   -> status={res['status']}, entries={res['entries']}, result={res['reason']}\n")

    # Summary
    print("\n========== SUMMARY ==========")
    ok_count = sum(1 for r in results if r["ok"])
    fail_count = len(results) - ok_count

    for r in results:
        status_str = f"{r['status']}" if r["status"] is not None else "-"
        flag = "✅" if r["ok"] else "❌"
        print(
            f"{flag} {r['name']}\n"
            f"   URL: {r['url']}\n"
            f"   HTTP: {status_str}, entries={r['entries']}, note={r['reason']}\n"
        )

    print(f"Total sources: {len(results)}, OK: {ok_count}, Failed: {fail_count}")

    # Non-zero exit code if any hard failures
    if fail_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
