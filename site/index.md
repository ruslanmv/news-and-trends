---
layout: "layout.njk"
title: "This Week"
---

{# Get latest news from most recent issue only (top 4) #}
{% set newsArticles = collections.latestNewsByIssue.slice(0, 4) %}
{# Get latest trend analysis #}
{% set latestTrend = collections.trend | first %}
{# Get the most recent date from content #}
{% set latestDate = (newsArticles[0] or latestTrend).date %}

{% if newsArticles.length > 0 or latestTrend %}

# Today's Tech News & Insights

<div class="meta">
  <span class="meta-pill">
    <span class="emoji">📅</span>
    <span>{{ latestDate | readableDate }}</span>
  </span>
  <span class="meta-pill">
    <span class="emoji">📰</span>
    <span>{{ newsArticles.length }} News + {% if latestTrend %}1 Trend{% else %}0 Trends{% endif %}</span>
  </span>
</div>

---

## 🔥 Trend Analysis

{% if latestTrend %}
<div style="background: linear-gradient(135deg, rgba(168, 85, 247, 0.15), rgba(56, 189, 248, 0.1)); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(168, 85, 247, 0.3); margin-bottom: 2rem;">
  <h3 style="margin-top: 0; color: #e879f9;">
    <a href="{{ latestTrend.url | url }}" style="color: inherit;">{{ latestTrend.data.title }}</a>
  </h3>
  <div style="color: #d1d5db; font-size: 0.95rem; margin-bottom: 1rem;">
    {{ latestTrend.content | striptags | truncate(250) | safe }}
  </div>
  <a class="primary-btn" href="{{ latestTrend.url | url }}" style="background: linear-gradient(135deg, #a855f7, #38bdf8);">
    Read Full Trend Analysis →
  </a>
</div>
{% else %}
<p style="color: var(--muted); font-style: italic;">Trend analysis coming soon...</p>
{% endif %}

---

## 📰 Latest News

{% if newsArticles.length > 0 %}
<div style="display: grid; gap: 1.5rem;">
  {% for article in newsArticles %}
  <div style="background: rgba(15, 23, 42, 0.6); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(148, 163, 184, 0.3); transition: all 0.2s ease;">
    <div style="display: flex; justify-content: space-between; align-items: start; gap: 1rem; margin-bottom: 0.75rem;">
      <h3 style="margin: 0; font-size: 1.15rem;">
        <a href="{{ article.url | url }}">{{ article.data.title }}</a>
      </h3>
      <span style="background: rgba(56, 189, 248, 0.2); color: #38bdf8; padding: 0.25rem 0.6rem; border-radius: 999px; font-size: 0.75rem; white-space: nowrap; font-weight: 600;">
        #{{ article.data.rank }}
      </span>
    </div>
    <div style="color: var(--muted); font-size: 0.85rem; margin-bottom: 0.5rem;">
      📍 {{ article.data.source }}
    </div>
    <div style="color: #d1d5db; font-size: 0.95rem; line-height: 1.5;">
      {{ article.content | truncate(200) | striptags | safe }}
    </div>
    <div style="margin-top: 1rem;">
      <a href="{{ article.url | url }}" style="font-size: 0.9rem; font-weight: 500;">
        Read more →
      </a>
    </div>
  </div>
  {% endfor %}
</div>
{% else %}
<p style="color: var(--muted); font-style: italic;">No news articles available yet.</p>
{% endif %}

---

## 📚 Archive

<div style="margin-top: 1.5rem;">
  <p style="color: var(--muted); margin-bottom: 1rem;">
    View all past news articles and trend analyses in the archive.
  </p>
  <a class="primary-btn" href="{{ '/archive/' | url }}">
    Browse Archive →
  </a>
</div>

{% if collections.issue and (collections.issue | length) > 0 %}
<div style="margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid rgba(148, 163, 184, 0.3);">
  <h3 style="font-size: 0.95rem; color: var(--muted); margin-bottom: 1rem;">Legacy Newsletter Issues</h3>
  <ul class="archive-list">
    {% for issue in collections.issue | reverse | slice(0, 3) %}
      <li>
        <a href="{{ issue.url | url }}">
          <strong>{{ issue.date | readableDate }}</strong> – {{ issue.data.title }}
        </a>
        <small>{{ issue.date | readableDate }}</small>
      </li>
    {% endfor %}
  </ul>
</div>
{% endif %}

{% else %}
# Welcome to TV.RUSLANMV News Network

<div class="content">
  <p>
    <strong>TV.RUSLANMV News &amp; Trends</strong> is your enterprise-grade source for
    cutting-edge AI &amp; technology news coverage. We deliver <strong>signal over noise</strong>.
  </p>

  <p>
    Our automated AI-powered news pipeline:
  </p>

  - 📡 Monitors leading AI &amp; technology sources 24/7
  - 🔥 Identifies breaking news and emerging trends in real-time
  - 📰 Generates comprehensive, publication-ready news briefings
  - 🌐 Publishes continuously via automated deployment

  <p>
    The latest news and trend analysis will appear here as soon as our AI agents complete
    the next cycle. Visit the <a href="{{ '/archive/' | url }}">archive</a> to explore
    all past news and trend reports.
  </p>
</div>
{% endif %}