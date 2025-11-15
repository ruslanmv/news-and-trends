module.exports = function (eleventyConfig) {
  // ---- Filters ----
  // Human-friendly date formatting for issue dates
  eleventyConfig.addFilter("readableDate", (dateObj) => {
    // Eleventy typically passes a Date object, but be robust:
    const d = new Date(dateObj);
    return d.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });
  });

  // You could add more enterprise-style filters here later (e.g. truncate, slug)

  return {
    dir: {
      input: ".",
      output: "docs", // GitHub Pages picks this up via the workflow artifact
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    // CRITICAL: site is served from https://ruslanmv.com/news-and-trends/
    pathPrefix: "/news-and-trends/",
  };
};
