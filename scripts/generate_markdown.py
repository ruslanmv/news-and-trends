#!/usr/bin/env python3
"""
generate_markdown.py

Uses a CrewAI multi-agent pipeline to turn the temporal JSON
(`data/issues/YYYY-MM-DD.json`) into a weekly Markdown newsletter
(`site/issues/YYYY-MM-DD.md`).

LLM configuration is handled in `llm_client.py` and typically points to:
- Ollama in CI (default, via OLLAMA_HOST / OLLAMA_MODEL)
- Or other providers locally (Watsonx, OpenAI, Claude, ...).
"""

import json
import os
from datetime import date
from glob import glob
from typing import Any, Dict, List

from crewai import Agent, Task, Crew, Process
from llm_client import llm  # Configured LLM instance


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMPORAL_DIR = os.path.join(BASE_DIR, "data", "issues")
OUTPUT_DIR = os.path.join(BASE_DIR, "site", "issues")


def find_latest_temporal() -> str:
    """
    Find the most recent temporal JSON file in data/issues/.

    Returns:
        Path to the latest JSON file.

    Raises:
        RuntimeError: If no JSON files are found.
    """
    pattern = os.path.join(TEMPORAL_DIR, "*.json")
    files = sorted(glob(pattern))
    if not files:
        raise RuntimeError(f"No temporal JSON files found in {TEMPORAL_DIR!r}")
    return files[-1]


def _build_articles_snippet(articles: List[Dict[str, Any]], limit: int = 15) -> str:
    """
    Build a truncated JSON snippet of articles to keep the prompt size under control.
    """
    trimmed = articles[:limit] if articles else []
    return json.dumps(trimmed, indent=2, ensure_ascii=False)


def run_news_crew(temporal_doc: Dict[str, Any]) -> str:
    """
    Run the CrewAI multi-agent system to produce a Markdown newsletter.

    Args:
        temporal_doc: Parsed JSON document containing:
            - issue_date
            - topic_of_week
            - top_terms
            - articles
            - by_source

    Returns:
        Markdown string for the weekly newsletter.

    Raises:
        RuntimeError: If the crew returns no usable result.
    """
    print("🤖 Starting CrewAI Multi-Agent System...")

    issue_date = temporal_doc.get("issue_date", "unknown date")
    topic_of_week = temporal_doc.get("topic_of_week", "AI & IT News")
    top_terms = temporal_doc.get("top_terms", [])
    articles: List[Dict[str, Any]] = temporal_doc.get("articles", []) or []

    if not articles:
        raise RuntimeError(
            "Temporal JSON contains no articles; cannot generate newsletter."
        )

    articles_snippet = _build_articles_snippet(articles, limit=15)

    # Handle top_terms being list of [term, count]
    top_terms_str = ", ".join(
        f"{t[0]} ({t[1]})" for t in top_terms if isinstance(t, (list, tuple)) and len(t) >= 2
    )

    # 1. Define Agents
    researcher = Agent(
        role="Senior News Researcher",
        goal="Identify the most important and high-impact articles for this weekly issue.",
        backstory=(
            "You receive a structured JSON array containing many AI/IT articles. "
            "You excel at filtering for relevance, impact, and signal over noise."
        ),
        llm=llm,
        verbose=True,
    )

    writer = Agent(
        role="Tech Newsletter Writer",
        goal=(
            "Write a concise, insightful weekly AI/IT briefing in Markdown "
            "for busy professionals who want signal, not hype."
        ),
        backstory=(
            "You write clear, engaging technical newsletters, summarizing complex topics "
            "in a way that is easy to scan yet informative."
        ),
        llm=llm,
        verbose=True,
    )

    # 2. Define Tasks
    research_task = Task(
        description=(
            f"You are given a JSON list of articles for this week (date: {issue_date}).\n"
            f"The computed 'Topic of the Week' is: {topic_of_week}\n"
            f"Top trending terms are: {top_terms_str or 'n/a'}\n\n"
            "From the article list, pick the 5–7 most important stories.\n"
            "For each, produce a short bullet with title, source, 1-sentence summary, and URL.\n\n"
            "JSON articles (truncated for context):\n"
            f"{articles_snippet}\n"
        ),
        expected_output=(
            "A Markdown bullet list of 5–7 key stories with:\n"
            "- bold title\n"
            "- source in parentheses\n"
            "- one-sentence explanation\n"
            "- URL in Markdown link format."
        ),
        agent=researcher,
    )

    write_task = Task(
        description=(
            "Using the researcher's list of key stories, write a full weekly newsletter in Markdown.\n"
            "The newsletter MUST have the following structure:\n"
            "1. H1 title for the week.\n"
            "2. A 2–3 sentence intro paragraph summarising the week.\n"
            f"3. A section '🔥 Topic of the Week: {topic_of_week}' (1–2 short paragraphs).\n"
            "4. A section '📰 Highlighted Articles' using the researcher's bullet list.\n"
            "5. A short 'Looking Ahead' paragraph about what might be important next week.\n\n"
            "Constraints:\n"
            "- Be professional, factual, and concise.\n"
            "- Do NOT fabricate articles or sources that are not in the JSON.\n"
            "- Use GitHub-flavored Markdown only, no YAML frontmatter.\n"
        ),
        expected_output="A complete weekly newsletter in Markdown format.",
        agent=writer,
        context=[research_task],
    )

    # 3. Define Crew
    news_crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        verbose=True,  # MUST be boolean in recent CrewAI versions
    )

    # 4. Run Crew
    print("🚀 Kicking off Crew... This may take a few minutes.")
    try:
        result = news_crew.kickoff()
    except Exception as exc:
        raise RuntimeError(f"CrewAI execution failed: {exc}") from exc

    if not result:
        raise RuntimeError("CrewAI returned an empty result.")

    # CrewAI versions may return a result object or a plain string.
    markdown: str
    if isinstance(result, str):
        markdown = result
    elif hasattr(result, "raw"):
        markdown = str(result.raw)
    else:
        markdown = str(result)

    markdown = markdown.strip()
    if not markdown:
        raise RuntimeError("CrewAI produced an empty Markdown string.")

    print("✅ CrewAI run complete.")
    return markdown


def write_markdown(issue_date: str, body_md: str) -> None:
    """
    Write the final Markdown newsletter file into site/issues/.

    Args:
        issue_date: Issue date string (YYYY-MM-DD).
        body_md: Markdown content (no frontmatter).
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, f"{issue_date}.md")

    frontmatter = (
        f"---\n"
        f'title: "Weekly Briefing – {issue_date}"\n'
        f"date: {issue_date}\n"
        f'layout: "layout.njk"\n'
        f"tags:\n"
        f"  - issue\n"
        f"---\n\n"
    )

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(frontmatter)
        f.write(body_md)

    print(f"✅ Markdown written to {out_path}")


def main() -> None:
    print("=========================================")
    print("  CREWAI – MARKDOWN GENERATOR (MULTI-LLM)")
    print("=========================================")

    latest_path = find_latest_temporal()
    print(f"Using temporal JSON: {latest_path}")

    with open(latest_path, "r", encoding="utf-8") as f:
        temporal_doc: Dict[str, Any] = json.load(f)

    issue_date = temporal_doc.get("issue_date") or date.today().isoformat()

    markdown = run_news_crew(temporal_doc)
    write_markdown(issue_date, markdown)


if __name__ == "__main__":
    main()
