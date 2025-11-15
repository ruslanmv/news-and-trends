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

  // Collection: News articles (type: news)
  eleventyConfig.addCollection("news", (collectionApi) => {
    return collectionApi.getAll().filter((item) => {
      return item.data.type === "news";
    });
  });

  // Collection: Trend analyses (type: trend)
  eleventyConfig.addCollection("trend", (collectionApi) => {
    return collectionApi.getAll().filter((item) => {
      return item.data.type === "trend";
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