# Daily Literature Digest — Design Document

**Date:** 2026-04-07
**Status:** Approved

## Goal

A daily automated pipeline that fetches ML/AI research papers and opportunities from multiple sources, summarizes them using Claude, stores them in a structured archive, generates a markdown report pushed to GitHub, and sends a Slack notification with highlights.

## Target Topics

- Mechanistic interpretability
- AI safety and alignment
- Language model personas
- Weird generalization (emergent misalignment, subliminal learning, superposition)
- General ML (broader coverage for context)

## Architecture

```
GitHub Actions (daily cron, 6am EST)
  1. FETCH        — query all sources, collect RawPaper objects
  2. DEDUPLICATE  — merge by DOI, then fuzzy title match (Levenshtein > 0.85)
  3. RANK         — Claude API scores relevance to target topics
  4. SUMMARIZE    — Claude API: 2-3 sentence summary, why it matters, 1-2 related papers with summaries
  5. WRITE        — generate report, update papers.json, write per-paper markdown, git push
  6. NOTIFY       — Slack webhook with top 5 highlights + link to full report
```

## Sources

### Group 1 — arXiv (arxiv Python package)
Seven keyword searches over last 24h:
- "mechanistic interpretability"
- "AI alignment"
- "AI safety"
- "language model personas"
- "emergent misalignment"
- "subliminal learning"
- "superposition features"

### Group 2 — Aggregator APIs
- **OpenAlex** — free REST API, no key, 250M papers, keyword search
- **Semantic Scholar** — REST API, free key, keyword search + recommendations

### Group 3 — Blogs & Community (RSS via feedparser)
- Alignment Forum
- LessWrong
- HuggingFace Daily Papers
- Transformer Circuits
- EleutherAI blog
- Anthropic research blog (community RSS)
- Anthropic alignment blog
- DeepMind blog
- OpenAI research blog
- Redwood Research blog
- BAIR blog

### Group 4 — Social
- **Reddit** (JSON endpoints) — r/MachineLearning, r/mlsafety, r/aisafety
- **Bluesky** — free public API, track AI safety researchers

### Group 5 — Newsletters (RSS/scraping)
- Import AI (web archive)
- The Gradient (RSS)
- CAIS Newsletter (web archive)

### Group 6 — Opportunities
- 80,000 Hours job board
- AI safety job boards
- Conference CFPs (NeurIPS, ICML, ICLR workshops)
- LinkedIn (RSS bridge / Apify for org pages)
- Alignment Forum / LessWrong job posts

### Skipped for v1
- Twitter/X (expensive API or fragile scrapers)

## Data Model

### RawPaper (fetcher output)
```python
@dataclass
class RawPaper:
    title: str
    authors: list[str]
    abstract: str
    url: str
    source: str           # "arxiv", "alignment_forum", etc.
    published_date: str   # ISO format
    doi: str | None
    tags: list[str]
```

### papers.json (structured index)
```json
[
  {
    "id": "2026-04-07_paper-slug",
    "title": "Paper Title",
    "authors": ["Author A", "Author B"],
    "url": "https://arxiv.org/abs/...",
    "doi": "10.xxxx/...",
    "source": "arxiv",
    "published_date": "2026-04-06",
    "fetched_date": "2026-04-07",
    "topics": ["mechanistic interpretability", "sparse autoencoders"],
    "relevance_score": 0.92,
    "summary_file": "papers/2026-04-07_paper-slug.md",
    "related_paper_ids": ["2024-03-15_related-slug"]
  }
]
```

### Per-paper markdown (papers/<slug>.md)
```markdown
---
title: Paper Title
authors: [Author A, Author B]
url: https://arxiv.org/abs/...
source: arxiv
published_date: 2026-04-06
topics: [mechanistic interpretability, sparse autoencoders]
relevance_score: 0.92
---

## Summary
2-3 sentences on the key contribution.

## Why It Matters
1-2 sentences connecting to target research interests.

## Related Papers
### [Related Paper 1](url) (2024)
2-3 sentence summary.

### [Related Paper 2](url) (2023)
2-3 sentence summary.
```

## Daily Report Format

```markdown
# Literature Guide — 2026-04-07

## Highlights
> Top 3-5 most relevant items with one-line teasers.

## Papers

### 1. [Paper Title](url)
**Authors:** A, B, C | **Source:** arXiv | **Date:** 2026-04-06
**Topics:** mechanistic interpretability, sparse autoencoders

**Summary:** 2-3 sentences.

**Why it matters:** 1-2 sentences.

**Related papers:**
- [Related 1](url) (2024) — 2-3 sentence summary
- [Related 2](url) (2023) — 2-3 sentence summary

---
(repeat for 10-20 items)

## Opportunities
### Jobs & Fellowships
- [Position](url) — Org, deadline

### Workshops & CFPs
- [Workshop](url) — Conference, deadline

### Grants & Programs
- [Program](url) — description

## Meta
- Sources checked: N
- Papers scanned: ~N
- Report generated: timestamp
```

## Slack Message Format

```
:newspaper: *Literature Guide — 2026-04-07*

*Top Papers:*
1. Paper Title — one-line summary
2. Paper Title — one-line summary
3. Paper Title — one-line summary

*Opportunities:* 3 new (2 jobs, 1 CFP)

:link: Full report: <github-link>
```

## File Structure

```
literature_guide/
├── .github/
│   └── workflows/
│       └── daily_digest.yml
├── src/
│   ├── __init__.py
│   ├── main.py                  # Pipeline orchestrator
│   ├── config.py                # Load config.yml + env vars
│   ├── fetchers/
│   │   ├── __init__.py
│   │   ├── arxiv.py
│   │   ├── openalex.py
│   │   ├── semantic_scholar.py
│   │   ├── rss.py
│   │   ├── reddit.py
│   │   ├── bluesky.py
│   │   ├── opportunities.py
│   │   └── newsletters.py
│   ├── dedup.py
│   ├── ranker.py
│   ├── summarizer.py
│   ├── report.py
│   ├── storage.py
│   └── notify.py
├── papers/
├── reports/
├── papers.json
├── config.yml
├── requirements.txt
└── README.md
```

## GitHub Actions Workflow

```yaml
name: Daily Literature Digest
on:
  schedule:
    - cron: '0 11 * * *'   # 6am EST / 7am EDT
  workflow_dispatch:

jobs:
  digest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install -r requirements.txt
      - run: python src/main.py
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
          SEMANTIC_SCHOLAR_API_KEY: ${{ secrets.SEMANTIC_SCHOLAR_API_KEY }}
      - uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "daily digest: ${{ env.TODAY }}"
```

## Secrets Required

| Secret | Source | Cost |
|--------|--------|------|
| ANTHROPIC_API_KEY | console.anthropic.com | ~$1-3/day (Sonnet) |
| SLACK_WEBHOOK_URL | Slack app settings | Free |
| SEMANTIC_SCHOLAR_API_KEY | semanticscholar.org/product/api | Free |

## Cost Estimate

- Claude API: 10-20 papers x ~2 calls each, ~$1-3/day with Sonnet
- GitHub Actions: ~5-10 min/run, well within free tier
- All other APIs: free

## Future Enhancements (not in v1)

- Twitter/X integration if API costs drop or reliable free scraping emerges
- Interactive Q&A mode (ask Claude questions about stored papers)
- Weekly/monthly trend summaries
- Citation graph visualization
- Email digest option
- Personalized relevance model that learns from which papers you engage with
