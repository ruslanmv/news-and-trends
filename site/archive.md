---
layout: "layout.njk"
title: "News & Trends Archive"
activeFilter: "all"
pagination:
  data: collections.issue
  size: 10
  reverse: true
  alias: issues
permalink: "archive/{% if pagination.pageNumber > 0 %}{{ pagination.pageNumber + 1 }}/{% endif %}index.html"
---

{% include "archive-cards.njk" %}
