---
layout: "layout.njk"
title: "Archive"
---

# Archive

Below are all news articles, trend analyses, and weekly issues, newest first.

<ul class="archive-list">
{%- for item in collections.issue | reverse -%}
  <li>
    <a href="{{ item.url | url }}">
      <strong>{{ item.date | readableDate }}</strong>
      {% if item.data.type == "trend" %}
        – <span class="category-badge trend-badge">Trend</span> {{ item.data.title }}
      {% elseif item.data.type == "news" %}
        – <span class="category-badge news-badge">News</span> {{ item.data.title }}
      {% else %}
        – {{ item.data.title }}
      {% endif %}
    </a>
    <small>
      {% if item.data.type == "news" and item.data.source %}
        {{ item.data.source }}
        {% if item.data.rank %} • #{{ item.data.rank }}{% endif %}
      {% elseif item.data.type == "trend" %}
        ML-based trend analysis
      {% else %}
        Weekly newsletter
      {% endif %}
    </small>
  </li>
{%- endfor -%}
</ul>