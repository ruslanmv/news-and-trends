---
layout: "layout.njk"
title: "Archive"
---

# Archive

Below are all weekly issues, newest first.

<ul class="archive-list">
{%- for issue in collections.issue | reverse -%}
  <li>
    <a href="{{ issue.url | url }}">
      <strong>{{ issue.date | readableDate }}</strong> – {{ issue.data.title }}
    </a>
    <small>Issue URL: {{ issue.url | url }}</small>
  </li>
{%- endfor -%}
</ul>
