module.exports = function (eleventyConfig) {
  return {
    dir: {
      input: ".",
      output: "docs" // GitHub Pages will serve from /docs
    },
    // Use Nunjucks for Markdown and HTML templates
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk"
  };
};
