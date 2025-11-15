#!/usr/bin/env python3
import json
import os
import re
import time
import feedparser
from collections import Counter, defaultdict
from datetime import datetime, date
from dateutil import parser as dateparser

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOURCES_FILE = os.path.join(BASE_DIR, "scripts", "sources.json")
OUTPUT_DIR = os.path.join(BASE_DIR, "data", "issues")

# Keywords / entities we care about for trends
TREND_KEYWORDS = [
    "LLM", "large language model", "Generative AI", "gen AI", "AGI",
    "OpenAI", "ChatGPT", "GPT-4", "GPT-5", "NVIDIA", "GPU", "Watsonx",
    "IBM", "Granite", "Claude", "Anthropic", "Google", "Gemini", "Meta",
    "Llama", "Mistral", "Quantum", "cybersecurity", "multimodal",
    "vector database", "RAG", "agent", "agentic", "AI safety", "regulation"
]


def load_sources():
    with open(SOURCES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def normalize_publish_date(entry):
    # Try RSS 'published', then 'updated'
    for key in ("published", "updated"):
        if key in entry:
            try:
                dt = dateparser.parse(entry[key])
                return dt.isoformat()
            except Exception:
                pass
    # fallback: now
    return datetime.utcnow().isoformat()


def fetch_all_articles():
    sources = load_sources()
    all_articles = []

    print("🛰️  Fetching news from sources...")
    for source in sources:
        name = source["name"]
        url = source["url"]
        weight = source.get("weight", 50)

        print(f"  -> {name}: {url}")
        try:
            feed = feedparser.parse(url)
            if feed.bozo:
                print(f"  ⚠️  Warning: issue parsing feed for {name}: {feed.bozo_exception}")
            entries = feed.entries[:10]  # top N per source

            for entry in entries:
                title = entry.get("title", "").strip()
                link = entry.get("link", "").strip()
                summary_raw = entry.get("summary", "") or entry.get("description", "") or ""
                # crude HTML strip: cut before first '<'
                summary = summary_raw.split("<")[0].strip()
                published = normalize_publish_date(entry)

                all_articles.append({
                    "title": title,
                    "link": link,
                    "summary": summary,
                    "source": name,
                    "source_weight": weight,
                    "published": published
                })

            print(f"     ✅ {len(entries)} entries ingested.")
            time.sleep(0.4)
        except Exception as e:
            print(f"  ⚠️  Failed to fetch {name}: {e}")

    print(f"\n📰 Total articles fetched: {len(all_articles)}")
    return all_articles


def extract_trends(articles):
    """Very simple trend extraction.
    - Look at titles and summaries
    - Count keyword mentions
    - Return 'topic_of_week' + top_terms (keyword, count)
    """
    if not articles:
        return "General AI & IT News", []

    text_blob = " ".join(
        (a["title"] or "") + " " + (a["summary"] or "")
        for a in articles
    )

    keyword_pattern = re.compile(
        r"(" + "|".join(re.escape(k) for k in TREND_KEYWORDS) + r")",
        re.IGNORECASE,
    )

    found = keyword_pattern.findall(text_blob)

    if not found:
        return "General AI & IT News", []

    norm_map = {k.lower(): k for k in TREND_KEYWORDS}
    normalized = [
        norm_map[x.lower()] for x in found if x.lower() in norm_map
    ]

    counts = Counter(normalized)
    topic_of_week, _ = counts.most_common(1)[0]
    top_terms = counts.most_common(10)

    return topic_of_week, top_terms


def score_articles(articles, top_terms):
    """Give each article a rough score combining:
    - source weight
    - presence of trending terms in title
    """
    top_term_set = {t[0].lower() for t in top_terms}
    for article in articles:
        score = article.get("source_weight", 50)
        title_lower = article["title"].lower()
        bonus = 0
        for term in top_term_set:
            if term in title_lower:
                bonus += 10
        article["score"] = score + bonus
    return sorted(articles, key=lambda a: a.get("score", 0), reverse=True)


def group_by_source(articles, limit_per_source=5):
    grouped = defaultdict(list)
    for a in articles:
        grouped[a["source"]].append(a)

    result = {}
    for s, items in grouped.items():
        result[s] = sorted(items, key=lambda a: a["score"], reverse=True)[:limit_per_source]
    return result


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    today = date.today().isoformat()  # e.g. "2025-11-15"
    output_path = os.path.join(OUTPUT_DIR, f"{today}.json")

    print("=======================================")
    print("  RETRIEVAL + TRENDS – TEMPORAL JSON   ")
    print("=======================================")

    articles = fetch_all_articles()
    topic_of_week, top_terms = extract_trends(articles)
    scored = score_articles(articles, top_terms)
    grouped = group_by_source(scored)

    temporal_doc = {
        "generated_at": datetime.utcnow().isoformat(),
        "issue_date": today,
        "topic_of_week": topic_of_week,
        "top_terms": top_terms,  # list of [term, count]
        "articles": scored,
        "by_source": grouped,
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(temporal_doc, f, indent=2)

    print(f"\n✅ Temporal source of truth written to {output_path}\n")


if __name__ == "__main__":
    main()
