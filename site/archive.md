---
layout: "layout.njk"
title: "Archive"
---

# Archive

Below are all weekly issues, newest first.

<ul class="archive-list">
{%- for issue in collections.issue | reverse -%}
  <li>
    <a href="{{ issue.url }}"><strong>{{ issue.date | date: "%Y-%m-%d" }}</strong> – {{ issue.data.title }}</a>
  </li>
{%- endfor -%}
</ul>
