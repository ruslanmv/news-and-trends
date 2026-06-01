---
layout: "layout.njk"
title: "Archive"
---

<section class="nt-digest">
  <p class="nt-kicker">Archive</p>
  <h2 class="nt-digest__date">Every issue, newest first</h2>
  <div class="nt-digest__meta">
    <span class="nt-pill"><i class="fas fa-folder-open"></i> {{ collections.issue | length }} entries</span>
    <span class="nt-pill"><i class="fas fa-newspaper"></i> {{ collections.news | length }} news</span>
    <span class="nt-pill"><i class="fas fa-chart-line"></i> {{ collections.trend | length }} trends</span>
  </div>
  <p class="nt-digest__note">Browse all daily updates, individual news articles, and ML-powered trend analyses.</p>
</section>

{% set issues = collections.issue | reverse %}

<div class="nt-section-head"><h2>All entries</h2></div>

<div class="nt-arch">
{% for item in issues %}
{% set isTrend = item.data.type == "trend" %}
{% set isNews = item.data.type == "news" %}
<a class="nt-archcard" href="{{ item.url | url }}">
  <div class="nt-archcard__head">
    {% if isTrend %}
      <span class="nt-badge nt-badge--trend">Trend Analysis</span>
    {% elif isNews %}
      <span class="nt-badge nt-badge--news">News</span>
    {% else %}
      <span class="nt-badge nt-badge--news">Daily Update</span>
    {% endif %}
    {% if isNews and item.data.rank %}<span class="nt-badge nt-badge--news">#{{ item.data.rank }}</span>{% endif %}
    <span class="nt-archcard__date">{{ item.date | readableDate }}</span>
    {% if isNews and item.data.source %}<span class="nt-archcard__date">· {{ item.data.source }}</span>{% endif %}
  </div>
  <h3 class="nt-archcard__title">{{ item.data.title }}</h3>
  <p class="nt-archcard__summary">{{ item.content | striptags | truncate(200) }}</p>
</a>
{% endfor %}
</div>
