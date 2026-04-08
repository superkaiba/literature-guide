# Literature Guide

Daily automated digest of ML/AI research papers and opportunities, focused on mechanistic interpretability, AI safety, alignment, and related topics.

## How It Works

A GitHub Actions workflow runs daily at 6am EST:

1. **Fetches** papers from arXiv, OpenAlex, Semantic Scholar, RSS blogs, Reddit, Bluesky, and newsletters
2. **Deduplicates** across sources using DOI matching and fuzzy title similarity
3. **Ranks** papers by relevance to target topics using Claude
4. **Summarizes** top 10-20 papers with key takeaways and related work
5. **Stores** each paper as structured markdown + JSON index
6. **Generates** a daily report in `reports/`
7. **Notifies** via Slack with highlights and a link to the full report

## Setup

1. Create a GitHub repo and push this code
2. Add secrets in repo Settings > Secrets:
   - `ANTHROPIC_API_KEY` — from console.anthropic.com
   - `SLACK_WEBHOOK_URL` — from Slack app settings
   - `SEMANTIC_SCHOLAR_API_KEY` — from semanticscholar.org/product/api
3. The workflow runs automatically, or trigger manually from Actions tab

## Local Development

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-...
export SLACK_WEBHOOK_URL=https://hooks.slack.com/...
python src/main.py
```

## Configuration

Edit `config.yml` to customize topics, sources, and thresholds.

## Structure

- `reports/` — Daily markdown reports
- `papers/` — Per-paper markdown files with summaries
- `papers.json` — Structured index of all papers
