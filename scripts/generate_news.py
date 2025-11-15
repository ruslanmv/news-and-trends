#!/usr/bin/env python3
"""
generate_news.py

Generates individual news articles (top 5) from the temporal JSON.
Each article is a separate markdown file with full content.

Output: site/issues/news-{date}-{index}.md (one per article)
"""

import html
import json
import os
import re
from datetime import date
from glob import glob
from typing import Any, Dict, List

from crewai import Agent, Task, Crew, Process
from llm_client import llm


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMPORAL_DIR = os.path.join(BASE_DIR, "data", "issues")
OUTPUT_DIR = os.path.join(BASE_DIR, "site", "issues")


def clean_text(value: str) -> str:
  """Decode HTML entities and strip whitespace."""
  if not value:
      return ""
  return html.unescape(value).strip()


def format_date_for_display(date_str: str) -> str:
  """Format ISO date string for display (remove time component)."""
  if not date_str:
      return ""
  if isinstance(date_str, str) and "T" in date_str:
      return date_str.split("T", 1)[0]
  return date_str


def find_latest_temporal() -> str:
  """Find the most recent temporal JSON file."""
  pattern = os.path.join(TEMPORAL_DIR, "*.json")
  files = sorted(glob(pattern))
  if not files:
      raise RuntimeError(f"No temporal JSON files found in {TEMPORAL_DIR!r}")
  return files[-1]


def slugify(text: str) -> str:
  """Convert text to URL-friendly slug."""
  text = text.lower()
  text = re.sub(r"[^\w\s-]", "", text)
  text = re.sub(r"[-\s]+", "-", text)
  return text[:50]


def generate_article(article: Dict[str, Any], rank: int, issue_date: str) -> str:
  """
  Use CrewAI to generate a full news article from a single article data.
  """
  title_raw = article.get("title", "Untitled")
  print(f"📝 Generating article {rank}: {title_raw[:60]}...")

  title = clean_text(title_raw)
  link = article.get("link", "")
  summary = clean_text(article.get("summary", ""))
  source = clean_text(article.get("source", "Unknown"))
  published = article.get("published", "")

  news_analyst = Agent(
      role="Senior News Analyst",
      goal="Analyze and expand news articles with context and implications",
      backstory=(
          "You are an experienced technology journalist who can take a brief news item "
          "and expand it into a comprehensive, informative article that explains the "
          "context, significance, and potential implications."
      ),
      llm=llm,
      verbose=False,
  )

  expand_task = Task(
      description=(
          f"Expand the following news item into a full article:\n\n"
          f"**Title**: {title}\n"
          f"**Source**: {source}\n"
          f"**Published**: {published}\n"
          f"**Summary**: {summary}\n"
          f"**URL**: {link}\n\n"
          "Write a clear, concise technology news article **in markdown** with this exact structure:\n\n"
          "## What happened\n"
          "- 1–2 short paragraphs that explain the core news event in plain language.\n\n"
          "## Why it matters\n"
          "- 1–2 paragraphs on the impact for the industry, users, or businesses.\n\n"
          "## Context & background\n"
          "- 1–2 paragraphs adding relevant history or competitive context.\n\n"
          "## What to watch next\n"
          "- 1 short paragraph on likely next steps, risks, or open questions.\n\n"
          "Guidelines:\n"
          "- Professional, neutral, journalist style (no hype, no marketing fluff).\n"
          "- Do NOT invent facts beyond what the summary implies.\n"
          "- Use short paragraphs and avoid repeating the same phrases.\n"
          "- Do not include a title or frontmatter; only the markdown sections above."
      ),
      expected_output="A 400–700 word markdown article with the specified section headings.",
      agent=news_analyst,
  )

  crew = Crew(
      agents=[news_analyst],
      tasks=[expand_task],
      process=Process.sequential,
      verbose=False,
  )

  try:
      result = crew.kickoff()

      if isinstance(result, str):
          markdown = result
      elif hasattr(result, "raw"):
          markdown = str(result.raw)
      else:
          markdown = str(result)

      return markdown.strip()

  except Exception as exc:
      print(f"  ⚠️  Error generating article: {exc}")
      return f"{summary}\n\n[Read more at {source}]({link})"


def write_article_file(
  article: Dict[str, Any],
  markdown_body: str,
  rank: int,
  issue_date: str
) -> str:
  """
  Write individual article markdown file.
  """
  os.makedirs(OUTPUT_DIR, exist_ok=True)

  title = clean_text(article.get("title", "Untitled"))
  source = clean_text(article.get("source", "Unknown"))
  link = article.get("link", "")
  published_raw = article.get("published", issue_date)
  published_display = format_date_for_display(published_raw)

  slug = slugify(title)
  filename = f"news-{issue_date}-{rank:02d}-{slug}.md"
  filepath = os.path.join(OUTPUT_DIR, filename)

  frontmatter = (
      f"---\n"
      f'title: "{title}"\n'
      f"date: {issue_date}\n"
      f"type: news\n"
      f"rank: {rank}\n"
      f'source: "{source}"\n'
      f'source_url: "{link}"\n'
      f"published: {published_raw}\n"
      f'layout: "layout.njk"\n'
      f"tags:\n"
      f"  - news\n"
      f"  - issue\n"
      f"---\n\n"
  )

  source_line = f"\n\n---\n\n**Source**: [{source}]({link})"
  if published_display:
      source_line += f" | Published: {published_display}"

  full_content = frontmatter + markdown_body + source_line

  with open(filepath, "w", encoding="utf-8") as f:
      f.write(full_content)

  print(f"  ✅ Written to {filename}")
  return filepath


def main() -> None:
  print("=" * 60)
  print("  INDIVIDUAL NEWS ARTICLE GENERATOR")
  print("=" * 60)

  latest_path = find_latest_temporal()
  print(f"Using temporal JSON: {latest_path}\n")

  with open(latest_path, "r", encoding="utf-8") as f:
      temporal_doc: Dict[str, Any] = json.load(f)

  issue_date = temporal_doc.get("issue_date") or date.today().isoformat()
  articles: List[Dict[str, Any]] = temporal_doc.get("articles", [])

  if not articles:
      raise RuntimeError("No articles found in temporal JSON")

  top_articles = articles[:5]

  print(f"Generating {len(top_articles)} individual news articles...\n")

  generated_files = []
  for rank, article in enumerate(top_articles, start=1):
      try:
          markdown_body = generate_article(article, rank, issue_date)
          filepath = write_article_file(article, markdown_body, rank, issue_date)
          generated_files.append(filepath)
      except Exception as exc:
          print(f"  ❌ Failed to generate article {rank}: {exc}")
          continue

  print(f"\n{'=' * 60}")
  print(f"✅ Generated {len(generated_files)} news articles")
  print(f"{'=' * 60}")


if __name__ == "__main__":
  main()
