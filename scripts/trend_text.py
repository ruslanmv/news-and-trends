#!/usr/bin/env python3
"""
trend_text.py — pure-stdlib helpers that turn untrusted LLM trend output into
clean Markdown, plus a pre-publish validation guard.

Kept dependency-free (no crewai / sklearn / numpy) so the parsing and validation
logic can be unit-tested in isolation and shared by both the generator
(``generate_trends.py``) and the one-off repair tool (``repair_trends.py``).

Design principle: LLM output is untrusted input — parse it, validate it, and
never publish it raw.
"""
from __future__ import annotations

import ast
import re
from typing import List, Tuple

# Body served when LLM output cannot be salvaged into clean Markdown.
SAFE_PLACEHOLDER_BODY = (
    "## Trend Analysis Temporarily Unavailable\n\n"
    "The automated trend analysis could not be parsed into clean Markdown for "
    "this issue. The underlying machine-learning metrics are still available in "
    "the methodology section below, and a fresh analysis will be generated on the "
    "next scheduled run."
)

# Signatures of an un-cleaned JSON/dict wrapper that must never reach the site.
UNSAFE_BODY_PATTERNS: Tuple[str, ...] = (
    r"^\s*\{",          # body starts with an object brace
    r'"body"\s*:',      # leftover "body": key
    r'"title"\s*:',     # leftover "title": key
    r'"""',             # python triple quotes
    r"'''",
)


def scan_json_string(text: str, start: int) -> Tuple[str, int]:
    """Scan a JSON double-quoted string starting at ``text[start] == '"'``.

    Handles standard escapes plus literal newlines. On an *unterminated* string
    (no closing quote — common in truncated LLM blobs) returns the accumulated
    content rather than discarding it. Returns ``(value, index_after_quote)`` or
    ``("", start)`` when ``start`` is not a quote.
    """
    if start >= len(text) or text[start] != '"':
        return "", start
    i = start + 1
    out: List[str] = []
    escapes = {'"': '"', "\\": "\\", "/": "/", "n": "\n", "t": "\t", "r": "\r", "b": "\b", "f": "\f"}
    while i < len(text):
        c = text[i]
        if c == "\\" and i + 1 < len(text):
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
        elif c == '"':
            return "".join(out), i + 1
        else:
            out.append(c)
            i += 1
    return ("".join(out), len(text)) if out else ("", start)


def extract_field(text: str, name: str) -> str:
    """Extract a top-level string field (``title`` / ``body``) from a possibly
    malformed JSON/dict blob. Supports standard JSON strings, Python-style
    triple-quoted strings (``\"\"\"`` / ``'''``), and unterminated values.
    Returns ``""`` when not found.
    """
    m = re.search(r'"' + re.escape(name) + r'"\s*:\s*', text)
    if not m:
        return ""
    start = m.end()
    for q in ('"""', "'''"):
        if text.startswith(q, start):
            end = text.find(q, start + 3)
            inner = text[start + 3:end] if end != -1 else text[start + 3:]
            return inner.strip()
    return scan_json_string(text, start)[0]


def recover_title_and_body(text: str) -> Tuple[str, str]:
    """Best-effort recovery of ``(title, body)`` from malformed JSON-ish output.

    Tries a well-formed Python literal first (handles complete dicts including
    triple-quoted strings), then falls back to field extraction that tolerates
    triple quotes and truncation.
    """
    try:
        obj = ast.literal_eval(text)
        if isinstance(obj, dict) and obj.get("body"):
            return str(obj.get("title", "")), str(obj["body"])
    except (ValueError, SyntaxError):
        pass
    return extract_field(text, "title"), extract_field(text, "body")


def dewrap_response(text: str) -> str:
    r"""Strip a leftover ``{ "title": .., "body": <triple-quote>`` head and the
    trailing ``<triple-quote> }`` so, at worst, clean-ish Markdown is published
    instead of the raw wrapper."""
    body = re.sub(
        r'^\s*\{?\s*"title"\s*:\s*"[^"]*"\s*,\s*"body"\s*:\s*(?:"""|\'\'\'|")',
        "", text, flags=re.DOTALL,
    )
    body = re.sub(r'(?:"""|\'\'\'|")\s*\}?\s*$', "", body, flags=re.DOTALL)
    return body.strip()


def is_unsafe_body(text: str) -> bool:
    """True if ``text`` still contains a raw JSON/dict wrapper signature."""
    return any(re.search(p, text, re.DOTALL) for p in UNSAFE_BODY_PATTERNS)


def validate_trend_body(markdown_body: str) -> str:
    """Final safety net: return clean Markdown — sanitising a wrapper if present,
    and falling back to :data:`SAFE_PLACEHOLDER_BODY` if it can't be cleaned.
    Logs loudly so CI surfaces the event."""
    if not is_unsafe_body(markdown_body):
        return markdown_body
    print("  🛑 Unsafe trend body detected before write — attempting to sanitise.")
    cleaned = dewrap_response(markdown_body)
    if cleaned and not is_unsafe_body(cleaned):
        print("  ✅ Sanitised wrapper from trend body.")
        return cleaned
    print("  ⚠️  Could not sanitise trend body — using safe placeholder instead.")
    return SAFE_PLACEHOLDER_BODY


# ---------------------------------------------------------------------------
# Markdown-first parsing (preferred path) — model-agnostic, no JSON contract.
# ---------------------------------------------------------------------------

_FENCE_RE = re.compile(r"^\s*```[a-zA-Z]*\s*\n(.*?)\n```\s*$", re.DOTALL)
_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)


def strip_code_fences(text: str) -> str:
    """Remove a single wrapping ``` ```lang ... ``` ``` fence if the whole
    response is fenced; otherwise return the text unchanged."""
    m = _FENCE_RE.match(text.strip())
    return m.group(1).strip() if m else text.strip()


def looks_jsonish(text: str) -> bool:
    """Heuristic: does this response look like a JSON/dict wrapper, not Markdown?"""
    head = text.lstrip()[:400]
    return head.startswith("{") or ('"body"' in head and '"title"' in head)


def _first_heading(text: str) -> Tuple[str, str]:
    """Return ``(title, body_without_that_heading)`` if the Markdown opens with a
    heading, else ``("", text)``. Only a *leading* heading is consumed, so the
    published title isn't duplicated at the top of the body."""
    stripped = text.lstrip("\n")
    m = _HEADING_RE.match(stripped)
    if m and stripped[:m.start()].strip() == "":
        title = m.group(1).strip().strip("*").strip()
        body = stripped[m.end():].lstrip("\n")
        return title, body
    return "", text


def parse_trend_output(text: str, fallback_title: str = "") -> Tuple[str, str]:
    """Turn raw LLM output into a clean ``(title, body)`` pair.

    Dual-mode and model-agnostic:
      * **Markdown** (preferred): body used as-is; title taken from a leading
        ``#``/``##`` heading, or ``fallback_title`` when absent.
      * **JSON / Python-dict** (legacy or other models): recovered via
        :func:`recover_title_and_body`, tolerating malformed/truncated blobs.

    The body always passes through :func:`validate_trend_body`, so a raw wrapper
    can never reach the published file.
    """
    cleaned = strip_code_fences(text)

    if looks_jsonish(cleaned):
        title, body = recover_title_and_body(cleaned)
        if not body:                       # nothing usable -> treat as Markdown
            title, body = _first_heading(cleaned)
    else:
        title, body = _first_heading(cleaned)

    title = (title or fallback_title or "AI Technology Trends: What's Emerging This Week").strip()
    body = validate_trend_body(body.strip())
    return title, body
