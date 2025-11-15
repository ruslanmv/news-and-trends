module.exports = function (eleventyConfig) {
  // Human-friendly date formatting for issue dates
  eleventyConfig.addFilter("readableDate", (dateObj) => {
    const d = new Date(dateObj);
    if (Number.isNaN(d.getTime())) return String(dateObj || "");
    return d.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });
  });

  // Truncate filter for content preview
  eleventyConfig.addFilter("truncate", (text, length = 200) => {
    if (!text || text.length <= length) return text;
    return text.substring(0, length) + "...";
  });

  // Strip HTML tags filter
  eleventyConfig.addFilter("striptags", (text) => {
    if (!text) return "";
    return text.replace(/<[^>]*>/g, "");
  });

  // All news posts (tag-based, robust)
  eleventyConfig.addCollection("news", (collectionApi) => {
    const items = collectionApi
      .getFilteredByTag("news")
      .sort((a, b) => a.date - b.date); // oldest -> newest
    return items;
  });

  // All trend posts (also tag-based)
  eleventyConfig.addCollection("trend", (collectionApi) => {
    const items = collectionApi
      .getFilteredByTag("trend")
      .sort((a, b) => a.date - b.date);
    return items;
  });

  // Latest-issue news only (used on home page)
  eleventyConfig.addCollection("latestNewsByIssue", (collectionApi) => {
    const allNews = collectionApi
      .getFilteredByTag("news")
      .sort((a, b) => a.date - b.date);

    if (!allNews.length) return [];

    // Take the newest date as the "current issue"
    const last = allNews[allNews.length - 1];
    if (!last.date || typeof last.date.toISOString !== "function") {
      return [];
    }
    const latestIso = last.date.toISOString().slice(0, 10);

    // Keep only news items from that same date
    const todaysNews = allNews.filter((item) => {
      if (!item.date || typeof item.date.toISOString !== "function") return false;
      return item.date.toISOString().slice(0, 10) === latestIso;
    });

    // Sort within the issue by rank (#1, #2, #3…)
    todaysNews.sort(
      (a, b) => (a.data.rank || 999) - (b.data.rank || 999)
    );

    return todaysNews;
  });

  return {
    dir: {
      input: ".",
      output: "docs", // GitHub Pages uses this via the workflow artifact
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    // Critical: project is at /news-and-trends/ (project pages)
    pathPrefix: "/news-and-trends/",
  };
};
