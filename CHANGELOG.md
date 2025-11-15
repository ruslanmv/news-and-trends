# Changelog

All notable changes to TechStatic Insights will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-15

### 🎉 Initial Release

#### Added

- **Multi-Source RSS Aggregation**
  - IBM Newsroom (AI section)
  - arXiv (AI and ML categories)
  - MIT Technology Review (AI section)
  - ScienceDaily (AI section)
  - Phys.org (Technology news)

- **CrewAI Multi-Agent System**
  - Senior News Researcher agent for content curation
  - Tech Newsletter Writer agent for content generation
  - Sequential task processing
  - Context-aware content generation

- **Multi-Provider LLM Support**
  - Ollama (default for CI/CD)
  - IBM Watsonx.ai
  - OpenAI (GPT-4 family)
  - Anthropic Claude
  - Environment-based configuration switching

- **Automated Trend Analysis**
  - Keyword frequency detection
  - Topic-of-the-week identification
  - Article relevance scoring
  - Source weight-based prioritization

- **GitHub Actions Automation**
  - Weekly scheduled runs (Fridays 08:00 UTC)
  - Manual workflow dispatch
  - Temporal Ollama environment in CI
  - Automatic content commit and deployment

- **Static Site Generation**
  - Eleventy-powered build system
  - Clean, professional design
  - Homepage with latest issue
  - Comprehensive archive page
  - Mobile-responsive layout

- **Data Management**
  - Temporal JSON storage (`data/issues/YYYY-MM-DD.json`)
  - Historical data preservation
  - Structured article metadata

- **Developer Experience**
  - Comprehensive Makefile commands
  - Multi-environment support
  - Clear documentation
  - Easy local development setup

#### Documentation

- Complete README with quick start guide
- Architecture diagrams and flow charts
- Configuration examples for all LLM providers
- Troubleshooting section
- Cost analysis
- Contributing guidelines
- MIT License

#### CI/CD

- GitHub Actions workflow for weekly automation
- Ollama installation in CI runners
- Model pulling and serving
- Content generation
- Static site build
- GitHub Pages deployment
- Automated commits

### Known Limitations

- RSS feeds must be publicly accessible (no authentication support)
- CrewAI generation can take 3-5 minutes depending on model
- GitHub Actions free tier limits apply (2,000 minutes/month)
- Ollama in CI limited to models that fit in runner memory

### Breaking Changes

- None (initial release)

---

## [Unreleased]

### Planned Features

- [ ] Email newsletter distribution
- [ ] Custom RSS feed authentication
- [ ] Enhanced analytics dashboard
- [ ] Multi-language support
- [ ] Advanced trend visualization
- [ ] API for programmatic access
- [ ] Webhook integrations
- [ ] Custom AI agent configurations

---

## Version History Summary

| Version | Date | Highlights |
|---------|------|------------|
| 1.0.0 | 2025-11-15 | Initial release with full automation |

---

*For more details on any release, see the [GitHub Releases](https://github.com/yourusername/news-trends-weekly/releases) page.*
