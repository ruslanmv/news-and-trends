---
layout: "layout.njk"
title: "News & Trends Archive — Trend Analysis"
activeFilter: "trend"
pagination:
  data: collections.trend
  size: 10
  alias: issues
permalink: "archive/trends/{% if pagination.pageNumber > 0 %}{{ pagination.pageNumber + 1 }}/{% endif %}index.html"
---

{% include "archive-cards.njk" %}
