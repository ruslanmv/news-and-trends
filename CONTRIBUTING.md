# Contributing to TechStatic Insights

First off, thank you for considering contributing to TechStatic Insights! It's people like you that make this project such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our commitment to providing a welcoming and inspiring community for all. Please be respectful and constructive in your interactions.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** to demonstrate the steps
- **Describe the behavior you observed** and what you expected
- **Include screenshots** if applicable
- **Provide your environment details** (OS, Python version, Node version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful** to most users
- **List any alternative solutions** you've considered

### Pull Requests

1. Fork the repository
2. Create a new branch from `main`:
   ```bash
   git checkout -b feature/my-new-feature
   ```
3. Make your changes
4. Test your changes thoroughly
5. Commit your changes using clear, descriptive commit messages
6. Push to your fork
7. Submit a pull request to the `main` branch

#### Pull Request Guidelines

- Follow the existing code style
- Write clear, concise commit messages
- Include comments in your code where necessary
- Update documentation if you're changing functionality
- Add tests for new features
- Ensure all tests pass before submitting

## Development Setup

### Prerequisites

- Python 3.10+
- Node.js 20+
- Git
- Ollama (for local testing)

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/news-trends-weekly.git
cd news-trends-weekly

# Install dependencies
make install

# Start Ollama (in another terminal)
ollama serve
ollama pull gemma:2b

# Set environment variables
export OLLAMA_API_BASE="http://127.0.0.1:11434"
export NEWS_LLM_MODEL="ollama/gemma:2b"

# Run the pipeline
make run
```

## Code Style

### Python

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise

Example:

```python
def fetch_articles(source_url: str, max_items: int = 10) -> list:
    """
    Fetch articles from an RSS feed.
    
    Args:
        source_url: The RSS feed URL
        max_items: Maximum number of items to fetch (default: 10)
        
    Returns:
        List of article dictionaries
    """
    # Implementation here
```

### JavaScript

- Use consistent indentation (2 spaces)
- Use semicolons
- Prefer `const` and `let` over `var`

## Testing

Before submitting a pull request:

```bash
# Run the full pipeline
make run

# Build the site
make build

# Serve locally and verify
make serve
```

Visit `http://localhost:8080` and verify:
- Homepage loads correctly
- Archive page lists all issues
- Individual issue pages render properly
- Links work correctly

## Areas for Contribution

We especially welcome contributions in these areas:

### High Priority

- [ ] Additional RSS feed sources
- [ ] Improved trend detection algorithms
- [ ] Better error handling and logging
- [ ] Unit tests for Python scripts
- [ ] Enhanced Eleventy templates
- [ ] Mobile-responsive design improvements

### Medium Priority

- [ ] Support for additional LLM providers
- [ ] Custom newsletter templates
- [ ] Email notification system
- [ ] Analytics integration
- [ ] SEO optimization
- [ ] Dark mode for the website

### Good First Issues

- [ ] Documentation improvements
- [ ] Adding new RSS sources
- [ ] Fixing typos
- [ ] Improving code comments
- [ ] Adding examples

## Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that don't affect code meaning (formatting, etc.)
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Performance improvement
- `test`: Adding missing tests
- `chore`: Changes to build process or auxiliary tools

### Examples

```
feat(rss): add support for Atom feeds

- Added Atom feed parser
- Updated sources.json schema
- Added tests for Atom parsing

Closes #123
```

```
fix(llm): correct Watsonx API endpoint

The previous endpoint was deprecated. Updated to use the new v1 API.

Fixes #456
```

## Questions?

Feel free to:

- Open an issue with your question
- Start a discussion in GitHub Discussions
- Reach out via email (see README for contact info)

## Recognition

Contributors will be recognized in:

- The project README
- Release notes
- GitHub contributors page

Thank you for contributing to TechStatic Insights! 🚀
