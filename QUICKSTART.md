# 🚀 Quick Start Guide

Get TechStatic Insights running in **5 minutes**!

## Prerequisites Checklist

- [ ] Git installed
- [ ] GitHub account
- [ ] Python 3.10+ installed
- [ ] Node.js 20+ installed

---

## Option 1: Deploy to GitHub (Recommended)

**Perfect for: Automated weekly newsletters with zero maintenance**

### Step 1: Upload to GitHub (2 minutes)

```bash
# Extract the ZIP
unzip news-trends-weekly.zip
cd news-trends-weekly

# Initialize git
git init
git add .
git commit -m "Initial commit: TechStatic Insights v1.0"

# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/news-trends-weekly.git
git branch -M main
git push -u origin main
```

### Step 2: Enable GitHub Pages (1 minute)

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under "Build and deployment":
   - Source: **GitHub Actions**
4. Click **Save**

### Step 3: Run First Workflow (2 minutes)

1. Go to **Actions** tab
2. Click **"Weekly News & Trends"** workflow
3. Click **"Run workflow"** → **"Run workflow"**
4. Wait 3-5 minutes for completion
5. Visit: `https://YOUR_USERNAME.github.io/news-trends-weekly/`

**🎉 Done! Your automated news digest is live!**

---

## Option 2: Run Locally (Development)

**Perfect for: Testing, customization, or local use**

### Step 1: Install Ollama (2 minutes)

Visit [ollama.ai](https://ollama.ai) and install for your OS.

Then:

```bash
# Start Ollama
ollama serve

# In another terminal, pull a model
ollama pull gemma:2b
```

### Step 2: Setup Project (2 minutes)

```bash
# Extract and enter directory
unzip news-trends-weekly.zip
cd news-trends-weekly

# Install dependencies
make install
```

### Step 3: Configure & Run (1 minute)

```bash
# Set environment variables
export OLLAMA_API_BASE="http://127.0.0.1:11434"
export NEWS_LLM_MODEL="ollama/gemma:2b"

# Run the pipeline
make run
```

**Output**: `data/issues/2025-XX-XX.json` and `site/issues/2025-XX-XX.md`

### Step 4: Build & Serve (1 minute)

```bash
# Build the site
make build

# Serve locally
make serve
```

**🎉 Done! Visit http://localhost:8080**

---

## Option 3: Use Premium LLM (Advanced)

### OpenAI Setup

```bash
export OPENAI_API_KEY="sk-..."
export NEWS_LLM_MODEL="openai/gpt-4o-mini"
make run
```

### Claude Setup

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
export NEWS_LLM_MODEL="anthropic/claude-3-5-sonnet-latest"
make run
```

### Watsonx Setup

```bash
export WATSONX_URL="https://us-south.ml.cloud.ibm.com"
export WATSONX_APIKEY="your-key"
export WATSONX_PROJECT_ID="your-project-id"
export NEWS_LLM_MODEL="watsonx/meta-llama/llama-3-1-70b-instruct"
make run
```

---

## 🔧 Customization Quick Tips

### Change News Sources

Edit `scripts/sources.json`:

```json
[
  {
    "name": "Your Source",
    "url": "https://example.com/rss",
    "weight": 100
  }
]
```

### Change Schedule

Edit `.github/workflows/weekly_news.yml`:

```yaml
schedule:
  - cron: "0 8 * * 5"  # Change this!
```

Use [crontab.guru](https://crontab.guru) to customize.

### Change Trend Keywords

Edit `scripts/retrieve_data.py`:

```python
TREND_KEYWORDS = [
    "Your", "Custom", "Keywords"
]
```

---

## 🐛 Troubleshooting

### "Connection refused" Error

**Problem**: Can't connect to Ollama

**Solution**:
```bash
# Check if Ollama is running
ollama list

# Start Ollama
ollama serve
```

### "No module named 'crewai'"

**Problem**: Dependencies not installed

**Solution**:
```bash
make install
# or
pip install -r scripts/requirements.txt
```

### GitHub Actions Fails

**Problem**: Workflow error

**Solution**:
1. Check Actions logs for specific error
2. Ensure `weekly_news.yml` is in `.github/workflows/`
3. Verify repository permissions are correct

### Empty Newsletter

**Problem**: No articles fetched

**Solution**:
```bash
# Test RSS feeds manually
python3 -c "import feedparser; print(feedparser.parse('https://newsroom.ibm.com/latest-news-artificial-intelligence?output=rss').entries[0].title)"
```

---

## ✅ Success Checklist

After deployment, verify:

- [ ] GitHub Pages site loads
- [ ] Homepage shows "This Week's Briefing"
- [ ] Archive page lists issues
- [ ] Clicking an issue shows the newsletter
- [ ] Links in newsletter work
- [ ] Site is mobile-friendly

---

## 📚 Next Steps

1. **Read the full README** for in-depth documentation
2. **Customize RSS sources** for your interests
3. **Adjust the schedule** to fit your needs
4. **Share your site** on social media
5. **Contribute** improvements back to the project

---

## 🆘 Need Help?

- **Documentation**: See [README.md](README.md)
- **Issues**: Check [Troubleshooting](#-troubleshooting) section
- **Questions**: Open a GitHub issue
- **Contributions**: See [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 🎉 Congratulations!

You now have a fully automated AI news digest running!

**What happens next:**

- ✅ **Every Friday at 8 AM UTC**: New content automatically generated
- ✅ **No maintenance required**: Runs completely hands-free
- ✅ **Always fresh**: Latest AI/IT news curated by AI
- ✅ **Professional output**: Publication-ready newsletters

**Share your deployment:**

- Tweet about it with #TechStaticInsights
- Add it to your portfolio
- Share with your team
- Star the repository ⭐

---

*Built with ❤️ - Happy automating!* 🚀
