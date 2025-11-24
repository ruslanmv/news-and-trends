---
layout: "layout.njk"
title: "Archive"
---

# News & Trends Archive

<div class="meta">
  <span class="meta-pill">
    <span class="emoji">🗂️</span>
    <span>{{ collections.issue | length }} Total Reports</span>
  </span>
  <span class="meta-pill">
    <span class="emoji">📰</span>
    <span>
      {{ collections.news | length }} News Articles
      &nbsp;•&nbsp;
      {{ collections.trend | length }} Trend Reports
    </span>
  </span>
</div>

<p style="color: var(--mm-text-muted); margin: 0 0 1.5rem;">
  Browse the complete history of AI & tech news coverage, trend analyses, and insights from TV.RUSLANMV. All reports are sorted by date, newest first.
</p>

<hr style="border-color: rgba(148, 163, 184, 0.35); margin: 1.5rem 0;" />

{% set issues = collections.issue | reverse %}

<div style="display: grid; gap: 1.5rem;">
{% for item in issues %}
{% set isTrend = item.data.type == "trend" %}
{% set isNews = item.data.type == "news" %}

<article
  style="padding: 1.25rem 1.5rem;
         border-radius: 14px;
         border: 1px solid rgba(148, 163, 184, 0.3);
         background: {% if isTrend %}linear-gradient(135deg, rgba(168, 85, 247, 0.15), rgba(56, 189, 248, 0.08)){% else %}rgba(15, 23, 42, 0.7){% endif %};
         box-shadow: 0 10px 25px rgba(15, 23, 42, 0.45);
         transition: transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease;"
  onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 16px 32px rgba(15,23,42,0.7)'; this.style.borderColor='rgba(148, 163, 184, 0.8)';"
  onmouseout="this.style.transform='none'; this.style.boxShadow='0 10px 25px rgba(15, 23, 42, 0.45)'; this.style.borderColor='rgba(148, 163, 184, 0.3)';"
>
  <header style="display: flex; justify-content: space-between; align-items: center; gap: 0.75rem; margin-bottom: 0.75rem;">
    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; align-items: center;">
      <span class="meta-pill" style="padding: 0.25rem 0.65rem; font-size: 0.8rem;">
        <span class="emoji">📅</span>
        <span>{{ item.date | readableDate }}</span>
      </span>

      {% if isTrend %}
        <span class="category-badge trend-badge" style="font-size: 0.75rem;">Trend Analysis</span>
      {% elseif isNews %}
        <span class="category-badge news-badge" style="font-size: 0.75rem;">News</span>
      {% else %}
        <span class="category-badge" style="font-size: 0.75rem;">Weekly Issue</span>
      {% endif %}

      {% if isNews and item.data.rank %}
        <span style="background: rgba(56, 189, 248, 0.18); color: #38bdf8; padding: 0.25rem 0.6rem; border-radius: 999px; font-size: 0.75rem; font-weight: 600;">
          #{{ item.data.rank }}
        </span>
      {% endif %}
    </div>

    {% if isNews and item.data.source %}
      <span style="color: var(--muted); font-size: 0.75rem; white-space: nowrap;">
        {{ item.data.source }}
      </span>
    {% endif %}
  </header>

  <h3 style="margin: 0 0 0.5rem; font-size: 1.1rem;">
    <a href="{{ item.url | url }}">
      {{ item.data.title }}
    </a>
  </h3>

  <div style="color: #d1d5db; font-size: 0.9rem; line-height: 1.5; margin-bottom: 0.75rem;">
    {{ item.content | striptags | truncate(220) | safe }}
  </div>

  <footer style="display: flex; justify-content: space-between; align-items: center; font-size: 0.8rem; color: var(--muted); margin-top: 0.5rem;">
    <span>
      {% if isNews and item.data.source %}
        📍 {{ item.data.source }}
        {% if item.data.rank %} • #{{ item.data.rank }}{% endif %}
      {% elseif isTrend %}
        🧠 ML-based trend analysis
      {% else %}
        🗞️ Weekly newsletter
      {% endif %}
    </span>

    <a href="{{ item.url | url }}" style="font-weight: 500; font-size: 0.8rem;">
      Open →
    </a>
  </footer>
</article>

{% endfor %}
</div>
