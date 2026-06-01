# Makefile for TechStatic Insights
# Default target
.DEFAULT_GOAL := help

PY := python3

.PHONY: help install install-python install-node run build build-all serve clean lint fmt check-sources test validate

help: ## Show this help message.
	@echo ""
	@echo "TechStatic Insights – Make targets"
	@echo "----------------------------------"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*## ' Makefile | sort | awk 'BEGIN {FS = ":.*## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "Tips:"
	@echo "  - uv detected automatically if installed (preferred)."
	@echo "  - Otherwise falls back to pip + requirements.txt."
	@echo ""

install: install-python install-node ## Install Python+Node dependencies (prefers uv).
	@echo "✅ All dependencies installed."

install-python: ## Install Python dependencies using uv if available, else pip.
	@if command -v uv >/dev/null 2>&1; then \
		echo "🔧 Using uv + pyproject.toml"; \
		uv sync; \
	else \
		echo "🔧 uv not found – falling back to pip + requirements.txt"; \
		$(PY) -m pip install --upgrade pip; \
		$(PY) -m pip install -r scripts/requirements.txt; \
	fi

install-node: ## Install Node dependencies for Eleventy site.
	@echo "📦 Installing Node dependencies in ./site ..."
	cd site && npm install

run: ## Fetch news and generate weekly issue, news articles, and ML trend insights via CrewAI.
	@if command -v uv >/dev/null 2>&1; then \
		echo "▶ Running with uv environment"; \
		uv run $(PY) scripts/retrieve_data.py; \
		uv run $(PY) scripts/generate_markdown.py; \
		uv run $(PY) scripts/generate_news.py; \
		uv run $(PY) scripts/generate_trends.py; \
	else \
		echo "▶ Running with system Python"; \
		$(PY) scripts/retrieve_data.py; \
		$(PY) scripts/generate_markdown.py; \
		$(PY) scripts/generate_news.py; \
		$(PY) scripts/generate_trends.py; \
	fi

test: ## Run unit tests, the content-safety gate, and a production build.
	@echo "🧪 [1/5] Compiling Python sources..."
	$(PY) -m py_compile scripts/*.py
	@echo "🧪 [2/5] Running trend-text unit tests..."
	$(PY) scripts/test_trends.py
	@echo "🧪 [3/5] Validating generated content (no raw LLM wrappers)..."
	$(PY) scripts/repair_trends.py --check
	@echo "🧪 [4/5] Smoke-importing the generator pipeline..."
	@if command -v uv >/dev/null 2>&1; then \
		( cd scripts && uv run --project .. $(PY) -c "import generate_trends; print('  generator imports OK')" ); \
	else \
		echo "  (skipped: uv not available — install heavy deps to run this check)"; \
	fi
	@echo "🧪 [5/5] Building Eleventy site..."
	cd site && npm run build
	@echo "✅ All tests passed."

validate: ## Fail if any generated trend file contains a raw LLM wrapper (CI gate).
	$(PY) scripts/repair_trends.py --check

build: install-node ## Build the static site (Eleventy -> site/docs).
	@echo "🏗  Building Eleventy site..."
	cd site && npm run build

build-all: ## Run full pipeline: fetch + generate (issue, news, trends) + build site.
	@echo "🚀 Running full content pipeline and site build..."
	$(MAKE) run
	$(MAKE) build
	@echo "✅ Full build complete. Site output is in ./site/docs"

serve: install-node ## Run Eleventy dev server on http://localhost:8080
	@echo "🌐 Starting local dev server on http://localhost:8080 ..."
	cd site && npm run start

clean: ## Remove build artifacts and Python cache.
	@echo "🧹 Cleaning build artifacts..."
	rm -rf site/docs
	rm -rf __pycache__ */__pycache__
	rm -rf .venv
	@echo "✅ Clean."

lint: ## Placeholder for future linting (Python/JS).
	@echo "ℹ️  No linters configured yet. Add flake8/ruff/eslint here if desired."

fmt: ## Placeholder for future auto-formatting.
	@echo "ℹ️  No formatters configured yet. Add black/isort/prettier here if desired."

check-sources: ## Health-check all RSS sources.
	@if command -v uv >/dev/null 2>&1; then \
		uv run $(PY) scripts/check_sources.py; \
	else \
		$(PY) scripts/check_sources.py; \
	fi
