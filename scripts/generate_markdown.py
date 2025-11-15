#!/usr/bin/env python3
import json
import os
from datetime import date
from glob import glob

from crewai import Agent, Task, Crew, Process
from llm_client import llm  # CrewAI LLM instance

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMPORAL_DIR = os.path.join(BASE_DIR, "data", "issues")
OUTPUT_DIR = os.path.join(BASE_DIR, "site", "issues")


def find_latest_temporal() -> str:
    files = sorted(glob(os.path.join(TEMPORAL_DIR, "*.json")))
    if not files:
        raise RuntimeError("No temporal JSON files found in data/issues/")
    return files[-1]


def run_news_crew(temporal_doc: dict) -> str:
    """
    Runs the CrewAI multi-agent system using the configured LLM
    (Ollama in CI by default, but can be Watsonx / OpenAI / Claude locally).
    """
    print("🤖 Starting CrewAI Multi-Agent System...")

    issue_date = temporal_doc.get("issue_date", "unknown date")
    topic_of_week = temporal_doc.get("topic_of_week", "AI & IT News")
    top_terms = temporal_doc.get("top_terms", [])
    articles = temporal_doc.get("articles", [])

    articles_snippet = json.dumps(articles[:15], indent=2)  # Cap for prompt size
    top_terms_str = ", ".join([f"{t[0]} ({t[1]})" for t in top_terms])

    # 1. Define Agents
    researcher = Agent(
        role="Senior News Researcher",
        goal="Identify the most important and high-impact articles for this weekly issue.",
        backstory=(
            "You read a structured JSON containing many AI/IT articles. "
            "You are great at filtering for relevance and impact."
        ),
        llm=llm,
        verbose=True,
    )

    writer = Agent(
        role="Tech Newsletter Writer",
        goal=(
            "Write a concise but insightful weekly AI/IT briefing in Markdown "
            "for busy professionals."
        ),
        backstory=(
            "You write clear and engaging technical newsletters, focusing on "
            "signal over noise and avoiding hype."
        ),
        llm=llm,
        verbose=True,
    )

    # 2. Define Tasks
    research_task = Task(
        description=(
            f"You are given a JSON list of articles for this week (date: {issue_date}).\n"
            f"The computed 'Topic of the Week' is: {topic_of_week}\n"
            f"Top trending terms are: {top_terms_str}\n\n"
            "From the article list, pick the 5-7 most important stories.\n"
            "For each, produce a short bullet with title, source, 1-sentence summary, and URL.\n\n"
            f"JSON articles (truncated):\n{articles_snippet}\n"
        ),
        expected_output=(
            "A Markdown bullet list of 5-7 key stories with title, source, "
            "one-sentence explanation, and URL."
        ),
        agent=researcher,
    )

    write_task = Task(
        description=(
            "Using the researcher's list of key stories, write a full weekly newsletter in Markdown.\n"
            "The newsletter must have this structure:\n"
            "1. H1 title for the week.\n"
            "2. A 2–3 sentence intro paragraph.\n"
            f"3. A section '🔥 Topic of the Week: {topic_of_week}' (1–2 paragraphs).\n"
            "4. A section '📰 Highlighted Articles' (the bulleted list from the researcher).\n"
            "5. A short 'Looking Ahead' paragraph.\n\n"
            "Be professional, concise, and stick to the provided info.\n"
            "Do NOT make up articles that do not exist in the JSON."
        ),
        expected_output="A complete Markdown newsletter file.",
        agent=writer,
        context=[research_task],
    )

    # 3. Define Crew
    news_crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        verbose=2,
    )

    # 4. Run Crew
    print("🚀 Kicking off Crew... This may take a few minutes.")
    result = news_crew.kickoff()

    if not result:
        raise RuntimeError("CrewAI returned no result.")

    print("✅ CrewAI run complete.")
    return result


def write_markdown(issue_date: str, body_md: str) -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, f"{issue_date}.md")

    frontmatter = f"""---
title: "Weekly Briefing – {issue_date}"
date: {issue_date}
layout: "layout.njk"
tags:
  - issue
---

"""

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(frontmatter)
        f.write(body_md)

    print(f"✅ Markdown written to {out_path}")


def main():
    print("=========================================")
    print("  CREWAI – MARKDOWN GENERATOR (MULTI-LLM)")
    print("=========================================")

    latest_path = find_latest_temporal()
    print(f"Using temporal JSON: {latest_path}")

    with open(latest_path, "r", encoding="utf-8") as f:
        temporal_doc = json.load(f)

    issue_date = temporal_doc.get("issue_date") or date.today().isoformat()

    markdown = run_news_crew(temporal_doc)
    write_markdown(issue_date, markdown)


if __name__ == "__main__":
    main()
