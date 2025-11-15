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

  // Collection: News articles (by tag)
  eleventyConfig.addCollection("news", (collectionApi) => {
    return collectionApi.getFilteredByTag("news").sort((a, b) => {
      return b.date - a.date; // newest first
    });
  });

  // Collection: Trend analyses (by tag)
  eleventyConfig.addCollection("trend", (collectionApi) => {
    return collectionApi.getFilteredByTag("trend").sort((a, b) => {
      return b.date - a.date; // newest first
    });
  });

  // Collection: Latest news from most recent issue only
  eleventyConfig.addCollection("latestNewsByIssue", (collectionApi) => {
    const newsItems = collectionApi.getFilteredByTag("news");
    if (newsItems.length === 0) return [];

    // Find the most recent date
    const latestDate = newsItems.reduce((max, item) => {
      const itemDate = new Date(item.data.date);
      return itemDate > max ? itemDate : max;
    }, new Date(0));

    // Filter only items from that date
    return newsItems
      .filter((item) => {
        const itemDate = new Date(item.data.date);
        return itemDate.toDateString() === latestDate.toDateString();
      })
      .sort((a, b) => {
        // Sort by rank if available
        const rankA = a.data.rank || 999;
        const rankB = b.data.rank || 999;
        return rankA - rankB;
      });
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