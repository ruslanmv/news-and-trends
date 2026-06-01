#!/usr/bin/env python3
"""
generate_trends.py

Uses traditional Machine Learning to analyze trends from collected news data.
Generates a trend analysis blog post with predictions and insights.

ML Techniques:
- TF-IDF for text feature extraction
- Topic modeling (NMF/LDA) for trend detection
- Clustering for grouping similar topics
- Time-based trend analysis

Output: site/issues/trend-{date}.md
"""

import html
import json
import os
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from glob import glob
from typing import Any, Dict, List, Tuple

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.cluster import KMeans

from crewai import Agent, Task, Crew, Process
from llm_client import llm
from trend_text import (
    recover_title_and_body,
    dewrap_response,
    validate_trend_body,
)


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMPORAL_DIR = os.path.join(BASE_DIR, "data", "issues")
OUTPUT_DIR = os.path.join(BASE_DIR, "site", "issues")


def clean_text(value: str) -> str:
    """Decode HTML entities and strip whitespace."""
    if not value:
        return ""
    return html.unescape(value).strip()


def load_recent_temporal_files(days: int = 30) -> List[Dict[str, Any]]:
    """
    Load recent temporal JSON files for historical trend analysis.

    Args:
        days: Number of days to look back

    Returns:
        List of temporal documents
    """
    pattern = os.path.join(TEMPORAL_DIR, "*.json")
    files = sorted(glob(pattern))

    if not files:
        raise RuntimeError(f"No temporal JSON files found in {TEMPORAL_DIR!r}")

    # Load recent files (at least the latest one)
    temporal_docs = []
    for filepath in files[-min(10, len(files)):]:  # Last 10 files max
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                temporal_docs.append(json.load(f))
        except Exception as e:
            print(f"⚠️  Error loading {filepath}: {e}")

    return temporal_docs


def extract_text_corpus(temporal_docs: List[Dict[str, Any]]) -> Tuple[List[str], List[Dict]]:
    """
    Extract text corpus from articles for ML analysis.

    Returns:
        (list of text documents, list of article metadata)
    """
    corpus = []
    metadata = []

    for doc in temporal_docs:
        articles = doc.get("articles", [])
        for article in articles:
            title = clean_text(article.get("title", ""))
            summary = clean_text(article.get("summary", ""))
            source = clean_text(article.get("source", ""))

            text = f"{title} {summary}"
            if text.strip():
                corpus.append(text)
                metadata.append({
                    "title": title,
                    "source": source,
                    "date": doc.get("issue_date", ""),
                    "score": article.get("score", 0)
                })

    return corpus, metadata


def perform_topic_modeling(corpus: List[str], n_topics: int = 5) -> Tuple[Any, Any, List[str]]:
    """
    Perform topic modeling using NMF.

    Returns:
        (model, tfidf_matrix, feature_names)
    """
    print("🧠 Performing topic modeling with NMF...")

    # TF-IDF vectorization
    tfidf = TfidfVectorizer(
        max_features=100,
        min_df=2,
        max_df=0.8,
        stop_words='english',
        ngram_range=(1, 2)
    )

    tfidf_matrix = tfidf.fit_transform(corpus)
    feature_names = tfidf.get_feature_names_out()

    # NMF for topic modeling
    nmf = NMF(n_components=n_topics, random_state=42, max_iter=300)
    nmf.fit(tfidf_matrix)

    return nmf, tfidf_matrix, feature_names


def extract_topics(model: Any, feature_names: List[str], n_words: int = 8) -> List[Tuple[int, List[str]]]:
    """
    Extract top words for each topic.

    Returns:
        List of (topic_id, top_words)
    """
    topics = []
    for topic_idx, topic in enumerate(model.components_):
        top_indices = topic.argsort()[-n_words:][::-1]
        top_words = [feature_names[i] for i in top_indices]
        topics.append((topic_idx, top_words))

    return topics


def perform_clustering(tfidf_matrix: Any, n_clusters: int = 5) -> Tuple[Any, np.ndarray]:
    """
    Perform K-means clustering on articles.

    Returns:
        (kmeans_model, cluster_labels)
    """
    print("🔍 Clustering articles...")

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(tfidf_matrix)

    return kmeans, labels


def analyze_temporal_trends(temporal_docs: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Analyze how trends change over time.

    Returns:
        Dictionary with trend insights
    """
    print("📈 Analyzing temporal trends...")

    keyword_timeline = defaultdict(list)

    for doc in temporal_docs:
        issue_date = doc.get("issue_date", "")
        top_terms = doc.get("top_terms", [])

        for term, count in top_terms:
            keyword_timeline[term].append({
                "date": issue_date,
                "count": count
            })

    # Identify trending up/down
    trends = {
        "rising": [],
        "declining": [],
        "stable": []
    }

    for term, timeline in keyword_timeline.items():
        if len(timeline) >= 2:
            recent_count = timeline[-1]["count"]
            older_count = timeline[0]["count"]

            change = recent_count - older_count
            if change > 5:
                trends["rising"].append((term, change))
            elif change < -5:
                trends["declining"].append((term, abs(change)))
            else:
                trends["stable"].append(term)

    # Sort by magnitude
    trends["rising"].sort(key=lambda x: x[1], reverse=True)
    trends["declining"].sort(key=lambda x: x[1], reverse=True)

    return trends


def generate_ml_insights(
    topics: List[Tuple[int, List[str]]],
    clusters: np.ndarray,
    temporal_trends: Dict[str, Any],
    latest_doc: Dict[str, Any]
) -> Tuple[str, str]:
    """
    Use CrewAI to generate a trend blog post based on ML insights.

    Returns:
        Tuple of (title, markdown_body)
    """
    print("✍️  Generating trend analysis blog post...")

    # Format ML insights for the prompt
    topics_str = "\n".join([
        f"Topic {idx + 1}: {', '.join(words[:5])}"
        for idx, words in topics
    ])

    rising_str = ", ".join([f"{term} (+{count})" for term, count in temporal_trends["rising"][:5]])
    declining_str = ", ".join([f"{term} (-{count})" for term, count in temporal_trends["declining"][:5]])

    n_clusters = len(set(clusters))
    cluster_distribution = Counter(clusters)
    clusters_str = ", ".join([f"Cluster {i}: {count} articles" for i, count in cluster_distribution.items()])

    topic_of_week = latest_doc.get("topic_of_week", "AI Technology")

    # Define specialized agents
    data_scientist = Agent(
        role="AI/ML Data Scientist",
        goal="Interpret machine learning results and identify meaningful patterns",
        backstory=(
            "You are a data scientist specializing in NLP and trend analysis. "
            "You excel at translating ML model outputs into actionable insights."
        ),
        llm=llm,
        verbose=False,
    )

    tech_blogger = Agent(
        role="Technology Trend Blogger",
        goal="Write engaging, insightful blog posts about technology trends",
        backstory=(
            "You write thought-provoking blog posts about emerging technology trends, "
            "helping readers understand where the industry is heading and why it matters."
        ),
        llm=llm,
        verbose=False,
    )

    # Tasks
    analyze_task = Task(
        description=(
            f"Analyze the following ML-derived insights from news data:\n\n"
            f"**Topic Modeling Results (NMF)**:\n{topics_str}\n\n"
            f"**Rising Trends**: {rising_str or 'None significant'}\n"
            f"**Declining Trends**: {declining_str or 'None significant'}\n\n"
            f"**Article Clustering**: {n_clusters} distinct clusters found\n"
            f"Distribution: {clusters_str}\n\n"
            f"**Current Top Topic**: {topic_of_week}\n\n"
            "Identify:\n"
            "1. The main theme emerging from the topics\n"
            "2. What the rising trends suggest about the industry direction\n"
            "3. What clusters reveal about different areas of focus\n"
            "4. A prediction for the next 1-2 months based on these patterns\n"
        ),
        expected_output=(
            "A structured analysis with:\n"
            "- Main emerging theme\n"
            "- Industry direction insights\n"
            "- Cluster interpretation\n"
            "- Short-term prediction"
        ),
        agent=data_scientist,
    )

    write_task = Task(
        description=(
            "Using the data scientist's analysis, create a compelling trend analysis.\n\n"
            "IMPORTANT: You MUST return your response as valid JSON with this exact structure:\n"
            "{\n"
            '  "title": "A catchy, topic-driven headline (8-12 words, NO generic date references)",\n'
            '  "body": "Full markdown blog post content"\n'
            "}\n\n"
            "Title requirements:\n"
            "- Must be specific to the actual trends discovered (NOT 'AI Trends Analysis')\n"
            "- Should capture the main emerging theme or pattern\n"
            "- Examples: 'The Rise of Agentic AI Systems', 'Quantum Computing Meets Machine Learning', "
            "'How Multimodal AI is Reshaping Enterprise Software'\n"
            "- NO dates in the title\n\n"
            "Body structure (markdown):\n"
            "1. **Introduction** (2-3 sentences): Set the context\n"
            "2. **Current Landscape** (2 paragraphs): What the ML analysis reveals\n"
            "3. **Emerging Patterns** (2 paragraphs): Deep dive into rising trends\n"
            "4. **Looking Forward** (1-2 paragraphs): Predictions\n"
            "5. **Conclusion** (1 paragraph): Key takeaways\n\n"
            "Style: Professional, data-driven, forward-looking, accessible.\n\n"
            "CRITICAL JSON RULES:\n"
            "- Return ONLY a single valid JSON object — no markdown code fences, no extra text.\n"
            '- The "body" value MUST be one JSON string with newlines escaped as \\n.\n'
            "- Do NOT use Python triple quotes (\"\"\" or ''') anywhere.\n"
            "- Escape any double quotes inside the text as \\\"."
        ),
        expected_output="Valid JSON with 'title' and 'body' keys",
        agent=tech_blogger,
        context=[analyze_task],
    )

    # Run crew
    crew = Crew(
        agents=[data_scientist, tech_blogger],
        tasks=[analyze_task, write_task],
        process=Process.sequential,
        verbose=False,
    )

    result = crew.kickoff()

    # Extract result text
    if isinstance(result, str):
        result_text = result
    elif hasattr(result, "raw"):
        result_text = str(result.raw)
    else:
        result_text = str(result)

    result_text = result_text.strip()

    # Try to parse as JSON
    try:
        # Remove markdown code blocks if present
        if result_text.startswith("```"):
            # Extract content between code blocks
            lines = result_text.split("\n")
            start_idx = 1 if lines[0].startswith("```") else 0
            end_idx = len(lines) - 1 if lines[-1].startswith("```") else len(lines)
            result_text = "\n".join(lines[start_idx:end_idx])

        parsed = json.loads(result_text)
        title = parsed.get("title", "")
        body = parsed.get("body", "")

        if not title or not body:
            raise ValueError("Missing title or body in JSON response")

        return clean_text(title), body.strip()

    except (json.JSONDecodeError, ValueError) as e:
        print(f"  ⚠️  Failed to parse JSON from LLM: {e}")
        # Tolerant recovery: the response is often a *malformed* (e.g. unterminated)
        # JSON blob. Pull the title/body strings out manually so we never publish
        # raw JSON to the site.
        title, body = recover_title_and_body(result_text)
        if body:
            print("  Recovered title/body from malformed JSON response")
            return clean_text(title), body.strip()
        # Last resort: never publish the raw wrapper. Strip any leftover
        # `{ "title": ..., "body": """` head and trailing `""" }` so the page
        # body is at least clean Markdown.
        print("  Using fallback title and a de-wrapped response body")
        body = dewrap_response(result_text)
        return clean_text(title) or "AI Technology Trends: What's Emerging This Week", body


def write_trend_file(title: str, markdown_body: str, issue_date: str, ml_metadata: Dict[str, Any]) -> str:
    """
    Write the trend analysis markdown file.

    Args:
        title: Generated title for the trend analysis
        markdown_body: Body content in markdown
        issue_date: Date string
        ml_metadata: Metadata about ML analysis

    Returns:
        Path to created file
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    filename = f"trend-{issue_date}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    frontmatter = (
        f"---\n"
        f'title: "{title}"\n'
        f"date: {issue_date}\n"
        f"type: trend\n"
        f'layout: "layout.njk"\n'
        f"tags:\n"
        f"  - trend\n"
        f"  - analysis\n"
        f"  - issue\n"
        f"ml_metadata:\n"
        f"  n_articles: {ml_metadata.get('n_articles', 0)}\n"
        f"  n_topics: {ml_metadata.get('n_topics', 0)}\n"
        f"  n_clusters: {ml_metadata.get('n_clusters', 0)}\n"
        f"---\n\n"
    )

    # Add methodology note
    methodology = (
        "\n\n---\n\n"
        "## Methodology\n\n"
        "This trend analysis is generated using traditional machine learning techniques:\n\n"
        "- **TF-IDF Vectorization**: Extract important terms from news articles\n"
        "- **Non-negative Matrix Factorization (NMF)**: Identify latent topics\n"
        "- **K-Means Clustering**: Group similar articles\n"
        "- **Temporal Analysis**: Track keyword trends over time\n\n"
        f"*Analysis based on {ml_metadata.get('n_articles', 0)} articles from recent news cycles.*"
    )

    # Final guard: never write a raw LLM wrapper to a published file.
    markdown_body = validate_trend_body(markdown_body)

    full_content = frontmatter + markdown_body + methodology

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_content)

    print(f"✅ Trend analysis written to {filename}")
    return filepath


def main() -> None:
    print("=" * 60)
    print("  ML-BASED TREND ANALYSIS GENERATOR")
    print("=" * 60)

    # Load recent temporal files
    temporal_docs = load_recent_temporal_files(days=30)
    latest_doc = temporal_docs[-1]
    issue_date = latest_doc.get("issue_date") or date.today().isoformat()

    print(f"Loaded {len(temporal_docs)} temporal files for analysis")
    print(f"Issue date: {issue_date}\n")

    # Extract corpus
    corpus, metadata = extract_text_corpus(temporal_docs)
    print(f"Extracted {len(corpus)} articles for ML analysis\n")

    if len(corpus) < 10:
        print("⚠️  Too few articles for robust ML analysis")
        n_topics = 3
        n_clusters = 3
    else:
        n_topics = 5
        n_clusters = 5

    # Perform ML analyses
    nmf_model, tfidf_matrix, feature_names = perform_topic_modeling(corpus, n_topics=n_topics)
    topics = extract_topics(nmf_model, feature_names, n_words=8)

    kmeans_model, cluster_labels = perform_clustering(tfidf_matrix, n_clusters=n_clusters)

    temporal_trends = analyze_temporal_trends(temporal_docs)

    # Display insights
    print("\n📊 ML Analysis Results:")
    print(f"  Topics discovered: {len(topics)}")
    print(f"  Clusters formed: {len(set(cluster_labels))}")
    print(f"  Rising trends: {len(temporal_trends['rising'])}")
    print(f"  Declining trends: {len(temporal_trends['declining'])}\n")

    # Generate blog post
    ml_metadata = {
        "n_articles": len(corpus),
        "n_topics": len(topics),
        "n_clusters": len(set(cluster_labels))
    }

    title, markdown = generate_ml_insights(topics, cluster_labels, temporal_trends, latest_doc)

    # Write file
    filepath = write_trend_file(title, markdown, issue_date, ml_metadata)

    print(f"\n{'=' * 60}")
    print("✅ Trend analysis complete")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()