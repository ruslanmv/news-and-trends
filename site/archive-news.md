---
layout: "layout.njk"
title: "News & Trends Archive — News"
activeFilter: "news"
pagination:
  data: collections.news
  size: 10
  alias: issues
permalink: "archive/news/{% if pagination.pageNumber > 0 %}{{ pagination.pageNumber + 1 }}/{% endif %}index.html"
---

{% include "archive-cards.njk" %}
