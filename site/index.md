---
layout: "layout.njk"
title: "This Week"
---

{% set latestIssue = collections.issue | reverse | first %}

{% if latestIssue %}
# This Week's Briefing – {{ latestIssue.date | date("%Y-%m-%d") }}

{{ latestIssue.content | safe }}

{% else %}
# Welcome

No issues have been generated yet. Once the first GitHub Action run completes, the latest weekly briefing will appear here.
{% endif %}