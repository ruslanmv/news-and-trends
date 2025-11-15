---
layout: "layout.njk"
title: "This Week"
---

{% set latestIssue = collections.issue | reverse | first %}

{% if latestIssue %}
# This Week’s Briefing – {{ latestIssue.date | readableDate }}

<div class="meta">
  <span class="meta-pill">
    <span class="emoji">📅</span>
    <span>Issue date: {{ latestIssue.date | readableDate }}</span>
  </span>
  <span class="meta-pill">
    <span class="emoji">📰</span>
    <span>Edition: {{ latestIssue.data.title }}</span>
  </span>
</div>

<div class="content">
  {{ latestIssue.content | safe }}

  <p style="margin-top: 1.5rem;">
    <a class="primary-btn" href="{{ latestIssue.url | url }}">
      Open this issue as a standalone article →
    </a>
  </p>
</div>

{% if collections.issue and (collections.issue | length) > 1 %}
## Recent previous issues

<ul class="archive-list">
  {% for issue in collections.issue | reverse %}
    {% if not loop.first and loop.index <= 4 %}
      <li>
        <a href="{{ issue.url | url }}">
          <strong>{{ issue.date | readableDate }}</strong> – {{ issue.data.title }}
        </a>
      </li>
    {% endif %}
  {% endfor %}
</ul>
{% endif %}

{% else %}
# Welcome to TechStatic Insights

<div class="content">
  <p>
    TechStatic Insights is an automated weekly AI &amp; IT briefing designed for
    technology leaders who want <strong>signal over noise</strong>.
  </p>

  <p>
    Each week, a multi-agent CrewAI pipeline:
  </p>

  - Aggregates news from leading AI &amp; technology sources  
  - Detects hot topics and emerging trends  
  - Generates a concise, publication-ready Markdown briefing  
  - Publishes to this static site via GitHub Pages  

  <p>
    Once the first GitHub Action run completes, the latest weekly briefing will appear here.
    In the meantime, you can visit the <a href="{{ '/archive/' | url }}">archive</a> page
    to see all generated issues.
  </p>
</div>
{% endif %}
