---
layout: "layout.njk"
title: "Today"
---

{# Latest news from the most recent issue only (top 4) #}
{% set newsArticles = collections.latestNewsByIssue.slice(0, 4) %}
{# Latest trend analysis #}
{% set latestTrend = collections.trend | first %}
{# Most recent date from content #}
{% set latestDate = (newsArticles[0] or latestTrend).date %}

{% if newsArticles.length > 0 or latestTrend %}

<section class="nt-digest">
  <div class="nt-digest__body">
    <p class="nt-kicker">Today’s AI &amp; Tech Insights</p>
    <h2 class="nt-digest__date">{{ latestDate | readableDate }}</h2>
    <div class="nt-digest__meta">
      <span class="nt-pill"><i class="fas fa-newspaper"></i> {{ newsArticles.length }} news</span>
      <span class="nt-pill"><i class="fas fa-chart-line"></i> {% if latestTrend %}1 trend{% else %}0 trends{% endif %}</span>
    </div>
    <p class="nt-digest__note">A snapshot of selected AI and technology news, curated and summarised by our team.</p>
  </div>

  <div class="nt-clock" id="ntClock" role="img" aria-label="Current local time in Rome, Italy">
    <div class="nt-clock__info">
      <div class="nt-clock__digital" id="ntDigitalTime">--:--</div>
      <div class="nt-clock__loc">
        Rome, Italy <span id="ntTimezone">(CEST)</span><br>
        Today, +0hrs
      </div>
    </div>
    <div class="nt-clock__analog" id="ntAnalogClock">
      <div class="nt-clock__hand nt-clock__hand--hour" id="ntHourHand"></div>
      <div class="nt-clock__hand nt-clock__hand--minute" id="ntMinuteHand"></div>
      <div class="nt-clock__hand nt-clock__hand--second" id="ntSecondHand"></div>
      <div class="nt-clock__dot"></div>
    </div>
  </div>
</section>

{% raw %}
<script>
(function () {
  var timeZone = "Europe/Rome";

  var digitalTime  = document.getElementById("ntDigitalTime");
  var timezoneLbl  = document.getElementById("ntTimezone");
  var hourHand     = document.getElementById("ntHourHand");
  var minuteHand   = document.getElementById("ntMinuteHand");
  var secondHand   = document.getElementById("ntSecondHand");
  var analogClock  = document.getElementById("ntAnalogClock");

  if (!analogClock) return;

  // Place the 1–12 numerals around the dial, scaled to the clock size.
  var size   = analogClock.offsetWidth || 150;
  var center = size / 2;
  var radius = center * 0.84;
  for (var i = 1; i <= 12; i++) {
    var num = document.createElement("div");
    num.className = "nt-clock__num";
    num.textContent = i;
    var angle = (i * 30 - 90) * Math.PI / 180;
    num.style.left = (center + radius * Math.cos(angle)) + "px";
    num.style.top  = (center + radius * Math.sin(angle)) + "px";
    analogClock.appendChild(num);
  }

  function getRomeTimeParts() {
    var formatter = new Intl.DateTimeFormat("en-GB", {
      timeZone: timeZone,
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
      hour12: false,
      timeZoneName: "short"
    });
    var parts = formatter.formatToParts(new Date());
    var get = function (type) {
      var p = parts.find(function (x) { return x.type === type; });
      return p ? p.value : "";
    };
    return {
      hour: Number(get("hour")),
      minute: Number(get("minute")),
      second: Number(get("second")),
      zone: get("timeZoneName")
    };
  }

  function pad(n) { return String(n).padStart(2, "0"); }

  function updateClock() {
    var t = getRomeTimeParts();
    digitalTime.textContent = pad(t.hour) + ":" + pad(t.minute);
    if (t.zone) timezoneLbl.textContent = "(" + t.zone + ")";

    var hourAngle   = ((t.hour % 12) * 30) + (t.minute * 0.5);
    var minuteAngle = t.minute * 6;
    var secondAngle = t.second * 6;

    hourHand.style.transform   = "translateX(-50%) rotate(" + hourAngle + "deg)";
    minuteHand.style.transform = "translateX(-50%) rotate(" + minuteAngle + "deg)";
    secondHand.style.transform = "translateX(-50%) rotate(" + secondAngle + "deg)";
  }

  updateClock();
  setInterval(updateClock, 1000);
})();
</script>
{% endraw %}

{% if latestTrend %}
<div class="nt-section-head">
  <h2>Featured Trend</h2>
  <a href="{{ latestTrend.url | url }}">View full analysis →</a>
</div>
<a class="nt-trend" href="{{ latestTrend.url | url }}">
  <p class="nt-kicker">Trend Analysis</p>
  <h3 class="nt-trend__title">{{ latestTrend.data.title }}</h3>
  <p class="nt-trend__summary">{{ latestTrend.content | striptags | truncate(260) }}</p>
  <span class="nt-cta">Read full trend analysis <i class="fas fa-arrow-right"></i></span>
</a>
{% endif %}

{% if newsArticles.length > 0 %}
<div class="nt-section-head">
  <h2>Latest News</h2>
  <a href="{{ '/archive/' | url }}">All news →</a>
</div>
<div class="nt-news">
  {% for article in newsArticles %}
  <a class="nt-newscard" href="{{ article.url | url }}">
    <span class="nt-newscard__num">{% if loop.index < 10 %}0{% endif %}{{ loop.index }}</span>
    <div>
      {% if article.data.source %}<p class="nt-newscard__source">{{ article.data.source }}</p>{% endif %}
      <h3 class="nt-newscard__title">{{ article.data.title }}</h3>
      <p class="nt-newscard__summary">{{ article.content | striptags | truncate(190) }}</p>
      <span class="nt-newscard__more nt-cta">Read more <i class="fas fa-arrow-right"></i></span>
    </div>
  </a>
  {% endfor %}
</div>
{% endif %}

<div class="nt-teaser">
  <p><strong>Browse the archive</strong> — every past briefing, news story, and trend analysis, newest first.</p>
  <a href="{{ '/archive/' | url }}">Browse previous issues <i class="fas fa-arrow-right"></i></a>
  <p style="margin-top:1rem;">Explore also: <a href="https://ruslanmv.com/Best-of-the-Best/">AI Rankings</a> — daily ranked AI repositories, papers, packages, courses, and tutorials.</p>
</div>

{% else %}

<section class="nt-digest">
  <p class="nt-kicker">Welcome</p>
  <h2 class="nt-digest__date">News &amp; Trends is warming up</h2>
  <p class="nt-digest__note">
    An automated multi-agent pipeline aggregates AI &amp; technology news, detects emerging
    trends, and publishes a concise daily briefing here. Once the first run completes, the
    latest digest will appear on this page. In the meantime, explore the
    <a href="{{ '/archive/' | url }}">archive</a>.
  </p>
</section>

{% endif %}
