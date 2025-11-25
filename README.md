<div align="center">

# 🤖 TechStatic Insights

### AI-Powered Daily Technology News Digest

*Fully automated, zero-maintenance tech newsletter powered by CrewAI multi-agent system*

[![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Powered by CrewAI](https://img.shields.io/badge/Powered%20by-CrewAI-FF6B6B?logo=robot&logoColor=white)](https://github.com/joaomdmoura/crewAI)
[![Built with Eleventy](https://img.shields.io/badge/Built%20with-Eleventy-222?logo=eleventy&logoColor=white)](https://www.11ty.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[Features](#-features) •
[Quick Start](#-quick-start) •
[Architecture](#-architecture) •
[Configuration](#-configuration) •
[Deployment](#-deployment)

</div>

---

## 📖 Overview

**TechStatic Insights** is a production-ready, fully automated AI news aggregation and curation platform that delivers daily technology briefings with zero manual intervention. It combines RSS feed aggregation, AI-powered content analysis, and multi-agent content generation to create professional newsletters automatically.

### Why TechStatic Insights?

- **🔄 Fully Automated**: Set it and forget it - runs daily via GitHub Actions
- **💰 Zero Cost**: Uses free Ollama models in CI (optional premium LLMs for local dev)
- **🧠 AI-Powered**: CrewAI multi-agent system for intelligent content curation
- **🔌 Multi-Provider**: Seamlessly switch between Ollama, OpenAI, Claude, or Watsonx
- **📊 Data-Driven**: Automated trend detection and relevance scoring
- **🚀 Production-Ready**: Clean code, comprehensive docs, best practices

---

## ✨ Features

### Core Capabilities

| Feature | Description |
|---------|-------------|
| **📰 Multi-Source Aggregation** | Pulls from IBM Newsroom, arXiv, MIT Tech Review, ScienceDaily, Phys.org |
| **🔍 Trend Analysis** | Automatic keyword extraction and trending topic detection |
| **🤖 Multi-Agent System** | Senior Researcher + Newsletter Writer agents collaborate |
| **📝 Professional Output** | Publication-ready Markdown newsletters with proper structure |
| **⏰ Scheduled Automation** | Daily GitHub Actions runs (customizable schedule) |
| **🌐 Static Site Generation** | Clean, fast Eleventy-powered website |
| **📦 Temporal Storage** | JSON-based data lake for historical analysis |

### LLM Provider Support

```
┌─────────────┬──────────────┬────────────┬──────────────┐
│   Ollama    │   Watsonx    │   OpenAI   │   Claude     │
│  (Default)  │    (IBM)     │  (GPT-4)   │ (Anthropic)  │
├─────────────┼──────────────┼────────────┼──────────────┤
│ ✅ Free     │ ✅ Enterprise│ ✅ Premium │ ✅ Premium   │
│ ✅ CI-Ready │ ✅ Scalable  │ ✅ Fast    │ ✅ Advanced  │
│ ✅ Local    │ ✅ Secure    │ ✅ Quality │ ✅ Quality   │
└─────────────┴──────────────┴────────────┴──────────────┘
```

---

## 🏗 Architecture

### System Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    GitHub Actions (Daily)                        │
└────────────────────────┬────────────────────────────────────────┘
                         │
         ┌───────────────┴───────────────┐
         │                               │
         ▼                               ▼
┌─────────────────┐            ┌─────────────────┐
│  RSS Retrieval  │            │  Ollama Setup   │
│  & Aggregation  │            │  (Temporal CI)  │
└────────┬────────┘            └────────┬────────┘
         │                               │
         │  ┌────────────────────────────┘
         │  │
         ▼  ▼
    ┌────────────────┐
    │ Trend Analysis │
    │  & Scoring     │
    └────────┬───────┘
             │
             ▼
    ┌────────────────────┐
    │  Temporal JSON     │
    │  data/issues/      │
    │  YYYY-MM-DD.json   │
    └────────┬───────────┘
             │
             ▼
    ┌────────────────────────┐
    │   CrewAI Multi-Agent   │
    │  ┌──────────────────┐  │
    │  │ News Researcher  │  │
    │  └────────┬─────────┘  │
    │           │             │
    │           ▼             │
    │  ┌──────────────────┐  │
    │  │ Newsletter Writer│  │
    │  └────────┬─────────┘  │
    └───────────┼─────────────┘
                │
                ▼
       ┌────────────────┐
       │   Markdown     │
       │ site/issues/   │
       │ YYYY-MM-DD.md  │
       └────────┬───────┘
                │
                ▼
       ┌────────────────┐
       │    Eleventy    │
       │  Static Build  │
       └────────┬───────┘
                │
                ▼
       ┌────────────────┐
       │ GitHub Pages   │
       │   Deployment   │
       └────────────────┘
```

### Project Structure

```
news-and-trends/
│
├── 📁 .github/workflows/
│   └── weekly_news.yml          # Automation pipeline
│
├── 📁 scripts/
│   ├── retrieve_data.py         # RSS aggregation + trend analysis
│   ├── generate_markdown.py     # CrewAI multi-agent system
│   ├── llm_client.py           # Multi-provider LLM config
│   ├── sources.json            # RSS feed configuration
│   └── requirements.txt        # Python dependencies
│
├── 📁 data/issues/
│   └── YYYY-MM-DD.json         # Temporal data storage
│
├── 📁 site/
│   ├── _includes/              # Eleventy templates
│   ├── _data/                  # Site configuration
│   ├── issues/                 # Generated newsletters
│   ├── index.md                # Homepage
│   └── archive.md              # Issue archive
│
├── Makefile                     # Development commands
└── README.md                    # This file
```

---

## 🚀 Quick Start

### Prerequisites

- **Git** (for version control)
- **Python 3.10+** (for scripts)
- **Node.js 20+** (for Eleventy)
- **Ollama** (for local development) OR API keys for cloud providers

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/ruslanmv/news-and-trends.git
cd news-and-trends
```

**2. Install dependencies**

```bash
make install
```

This installs:
- Python packages (CrewAI, feedparser, numpy, etc.)
- Node packages (Eleventy)

**3. Configure your LLM provider**

Choose one of the following options:

<details>
<summary><b>Option A: Local Ollama (Recommended for Development)</b></summary>

```bash
# Start Ollama in a separate terminal
ollama serve
ollama pull gemma:2b

# Set environment variables
export OLLAMA_API_BASE="http://127.0.0.1:11434"
export NEWS_LLM_MODEL="ollama/gemma:2b"
```

**Pros:** Free, fast, no API keys needed  
**Cons:** Requires local installation
</details>

<details>
<summary><b>Option B: OpenAI GPT-4</b></summary>

```bash
export OPENAI_API_KEY="sk-your-api-key-here"
export NEWS_LLM_MODEL="openai/gpt-4o-mini"
```

**Pros:** High quality, reliable  
**Cons:** Costs per token
</details>

<details>
<summary><b>Option C: Anthropic Claude</b></summary>

```bash
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
export NEWS_LLM_MODEL="anthropic/claude-3-5-sonnet-latest"
```

**Pros:** Excellent reasoning, long context  
**Cons:** Costs per token
</details>

<details>
<summary><b>Option D: IBM Watsonx.ai</b></summary>

```bash
export WATSONX_URL="https://us-south.ml.cloud.ibm.com"
export WATSONX_APIKEY="your-watsonx-apikey"
export WATSONX_PROJECT_ID="your-project-id"
export NEWS_LLM_MODEL="watsonx/meta-llama/llama-3-1-70b-instruct"
```

**Pros:** Enterprise-ready, scalable, IBM support  
**Cons:** Requires IBM Cloud account
</details>

**4. Run the pipeline locally**

```bash
# Fetch news and generate content
make run

# Build the static site
make build

# Serve locally at http://localhost:8080
make serve
```

---

## ⚙️ Configuration

### RSS Feed Sources

Edit `scripts/sources.json` to customize news sources:

```json
[
  {
    "name": "Your Source Name",
    "url": "https://example.com/rss",
    "weight": 100
  }
]
```

**Weight**: Higher values = more influential in trend detection (0-100 recommended)

### Trend Keywords

Modify `TREND_KEYWORDS` in `scripts/retrieve_data.py`:

```python
TREND_KEYWORDS = [
    "LLM", "Generative AI", "OpenAI", "ChatGPT",
    "Your", "Custom", "Keywords"
]
```

### Scheduling

Adjust the cron schedule in `.github/workflows/weekly_news.yml`:

```yaml
on:
  schedule:
    - cron: "0 8 * * *"  # Every day at 08:00 UTC
```

Use [crontab.guru](https://crontab.guru/) to customize timing.

---

## 🚢 Deployment

### GitHub Pages Setup

**1. Push to GitHub**

```bash
git add .
git commit -m "Initial setup"
git push origin main
```

**2. Enable GitHub Pages**

1. Go to **Settings** → **Pages**
2. Under "Build and deployment", select **GitHub Actions**
3. Save

**3. Configure Secrets (Optional)**

For cloud LLM providers, add secrets:

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Add repository secrets:
   - `OPENAI_API_KEY`
   - `ANTHROPIC_API_KEY`
   - `WATSONX_APIKEY`
   - `WATSONX_URL`
   - `WATSONX_PROJECT_ID`

**4. Trigger First Run**

- Go to **Actions** tab
- Select "Daily News & Trends"
- Click "Run workflow"
- Watch the magic happen! ✨

### CI/CD Pipeline

The GitHub Actions workflow automatically:

1. ✅ Installs Ollama in the runner
2. ✅ Pulls the gemma:2b model
3. ✅ Fetches news from RSS feeds
4. ✅ Analyzes trends
5. ✅ Generates newsletter via CrewAI
6. ✅ Commits new content
7. ✅ Builds static site
8. ✅ Deploys to GitHub Pages

**Zero configuration required** - it just works!

---

## 💡 Usage Examples

### Local Development Commands

```bash
# Install all dependencies
make install

# Run data retrieval + content generation
make run

# Build the static site
make build

# Serve locally (with hot reload)
make serve

# Clean build artifacts
make clean
```

### Testing Different LLM Providers

```bash
# Test with Ollama
export NEWS_LLM_MODEL="ollama/llama2"
make run

# Test with GPT-4
export NEWS_LLM_MODEL="openai/gpt-4o"
make run

# Test with Claude
export NEWS_LLM_MODEL="anthropic/claude-3-5-sonnet-latest"
make run
```

---

## 🎯 How It Works

### 1. Data Retrieval (`retrieve_data.py`)

- Fetches articles from configured RSS sources
- Normalizes publish dates
- Extracts summaries (HTML-stripped)
- Scores articles based on source weight + keyword relevance
- Detects trending topics via keyword frequency analysis
- Saves structured JSON to `data/issues/YYYY-MM-DD.json`

### 2. Content Generation (`generate_markdown.py`)

**Multi-Agent System:**

```python
Agent 1: Senior News Researcher
├─ Role: Filter and rank articles
├─ Goal: Identify 5-7 most impactful stories
└─ Output: Curated article list

Agent 2: Tech Newsletter Writer
├─ Role: Write professional newsletter
├─ Goal: Create engaging, informative briefing
├─ Input: Researcher's curated list
└─ Output: Complete Markdown newsletter
```

**Newsletter Structure:**

1. H1 Daily Title
2. Introduction (2-3 sentences)
3. 🔥 Trending Topic (1-2 paragraphs)
4. 📰 Highlighted Articles (bulleted list)
5. Looking Ahead (closing paragraph)

### 3. Static Site Build (Eleventy)

- Converts Markdown to HTML
- Applies professional template
- Generates homepage (latest issue)
- Creates archive page (all issues)
- Outputs to `site/docs/` for GitHub Pages

---

## 🔧 Troubleshooting

<details>
<summary><b>Ollama connection errors</b></summary>

**Problem:** `Connection refused to localhost:11434`

**Solution:**
```bash
# Check if Ollama is running
ollama list

# Start Ollama server
ollama serve

# Verify model is pulled
ollama pull gemma:2b
```
</details>

<details>
<summary><b>GitHub Actions failing</b></summary>

**Problem:** Workflow fails during Ollama setup

**Solution:**
- Check the Actions logs for specific errors
- Ensure `weekly_news.yml` has correct permissions
- Verify the workflow file is in `.github/workflows/`
- Try manual trigger first before relying on schedule
</details>

<details>
<summary><b>No articles being fetched</b></summary>

**Problem:** Empty or error-filled JSON output

**Solution:**
```bash
# Test RSS feeds manually
python3 -c "import feedparser; print(feedparser.parse('https://newsroom.ibm.com/latest-news-artificial-intelligence?output=rss').entries[0])"

# Check sources.json for valid URLs
cat scripts/sources.json

# Increase timeout if network is slow
```
</details>

<details>
<summary><b>CrewAI taking too long</b></summary>

**Problem:** Generation times > 10 minutes

**Solution:**
- Switch to a faster model (e.g., `gemma:2b` instead of `llama2:13b`)
- Reduce article count in `generate_markdown.py` (line 32)
- Use `temperature=0.5` for faster, more deterministic output
</details>

---

## 📊 Cost Analysis

### Ollama (Default)

| Resource | Cost | Notes |
|----------|------|-------|
| GitHub Actions | **$0** | Free tier: 2,000 min/month |
| Ollama Model | **$0** | Open-source models |
| GitHub Pages | **$0** | Unlimited for public repos |
| **Total** | **$0/month** | 🎉 Completely free! |

### Cloud Providers (Optional)

| Provider | Model | Cost/Newsletter | Monthly (30x) |
|----------|-------|-----------------|--------------|
| OpenAI | gpt-4o-mini | ~$0.05 | ~$1.50 |
| Claude | Sonnet 3.5 | ~$0.15 | ~$4.50 |
| Watsonx | Llama 3.1 70B | ~$0.10 | ~$3.00 |

*Estimates based on ~5K input + 2K output tokens per run*

---

## 🤝 Contributing

We welcome contributions! Here's how:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code
- Use meaningful commit messages
- Add tests for new features
- Update documentation

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **[CrewAI](https://github.com/joaomdmoura/crewAI)** - Multi-agent orchestration framework
- **[Ollama](https://ollama.ai/)** - Local LLM runtime
- **[Eleventy](https://www.11ty.dev/)** - Static site generator
- **[LiteLLM](https://github.com/BerriAI/litellm)** - Multi-provider LLM proxy

---

## 📞 Support

- 📧 **Email**: contact@ruslanmv.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/ruslanmv/news-and-trends/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/ruslanmv/news-and-trends/discussions)

---

<div align="center">

**Built with ❤️ by the TechStatic Team**

⭐ **Star this repo** if you find it useful!

[Report Bug](https://github.com/ruslanmv/news-and-trends/issues) •
[Request Feature](https://github.com/ruslanmv/news-and-trends/issues) •
[Documentation](https://github.com/ruslanmv/news-and-trends/wiki)

</div>
