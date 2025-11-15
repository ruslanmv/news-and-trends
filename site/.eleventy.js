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
