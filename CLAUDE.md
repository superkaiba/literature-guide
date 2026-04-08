# Literature Guide — Claude Code Daily Digest

This repo is a daily ML/AI literature digest. Claude Code IS the pipeline — no Python scripts needed. When triggered, Claude Code searches the web, analyzes papers, writes reports, commits, pushes, and sends email.

## Daily Digest Workflow

When prompted to run the daily digest, execute these steps:

### Step 1: Search for Papers (use subagents in parallel)

Dispatch multiple subagents to search these sources simultaneously. Today's date should be used for all file naming.

**arXiv searches** (one subagent per query):
- "mechanistic interpretability" 2026
- "AI alignment" 2026
- "AI safety" 2026
- "language model personas" 2026
- "emergent misalignment" 2026
- "subliminal learning" 2026
- "superposition features" 2026

**Blog/org searches** (one subagent for all):
- Alignment Forum recent posts
- LessWrong recent posts
- HuggingFace Daily Papers
- Transformer Circuits (transformer-circuits.pub)
- EleutherAI blog
- Anthropic Research blog
- DeepMind blog
- OpenAI Research blog
- Redwood Research blog
- BAIR blog

**Reddit** (one subagent):
- r/MachineLearning top posts this week
- r/mlsafety recent
- r/aisafety recent

**Newsletters** (one subagent):
- Import AI latest
- The Gradient latest
- CAIS Newsletter latest

**Opportunities** (one subagent):
- 80,000 Hours job board — AI safety roles
- aisafety.world — events, fellowships, workshop CFPs

Each search subagent should return: title, authors, URL, source, and a 2-sentence summary of why it's interesting.

### Step 2: Deduplicate and Rank

From all search results, deduplicate by title similarity. Then select the top 10-20 papers using two criteria:
1. **Topic relevance** to core interests: mechanistic interpretability, AI safety, alignment, language model personas, emergent misalignment, subliminal learning, superposition features
2. **General importance** — landmark papers from Anthropic, DeepMind, OpenAI, Meta, Google Brain should ALWAYS be included even if outside core topics

### Step 3: Deep Analysis (use subagents in parallel)

For each selected paper, dispatch a subagent to produce a rich analysis. The subagent should:

1. **Web-search the paper URL** to read the abstract/full text
2. **Web-search each author** for affiliations, h-index, notable prior work
3. **Web-search for discussion** of the paper (Twitter/X, Reddit, blog posts)

Then produce this structured analysis:

```markdown
---
title: "Paper Title"
authors: ['Author 1', 'Author 2']
url: https://...
source: arxiv|blog|reddit|newsletter
published_date: YYYY-MM-DD
document_type: preprint|published|blog_post|forum_post
topics: ['mechanistic interpretability', ...]
relevance_score: 0.0-1.0
confidence: high|medium|low
version_info: "v1 (first release)" or "v2 — revised YYYY-MM-DD, originally posted YYYY-MM-DD"
code_available: true|false|unknown
triage: "read in full"|"read abstract + key findings"|"awareness only"
---

# Paper Title

## Plain Language Summary
3-5 sentences, no jargon, explain like talking to a smart friend.
Start with "So what — why should anyone care?" framing.

## Confidence & Provenance
A structured assessment of how much to trust this paper:
- **Confidence: HIGH/MEDIUM/LOW** — one-line rationale
- **Author credibility:** Senior author's h-index, top prior papers, lab reputation
- **Venue/status:** Peer-reviewed (where?), preprint, blog post, etc.
- **Version:** First release, or revision? If revision, what changed? (web-search arXiv version history)
- **Code/data:** Released? Link if available. "No code" is a yellow flag for empirical papers.
- **Replication/discussion:** Has anyone independently validated, criticized, or extended this? (web-search)

## Triage Recommendation
One of: **Read in full** / **Read abstract + key findings** / **Awareness only**
Brief justification (1 sentence): why this level of attention.

## About the Authors
Web-searched: affiliations, notable prior work, h-index, citation counts.
Flag if any author has a history of retracted or controversial work.

## Overview
What this paper is and its context.

## Main Goal
What the authors set out to show/prove/build.

## Key Findings
- Finding 1: ...
- Finding 2: ...
- Finding 3: ...
(3-5 bullets)

## Methodology
How they did it. Models used, datasets, evaluation approach.

## What's Novel
What's genuinely new here vs. incremental.

## Limitations & Open Questions
Honest assessment of weaknesses.

## Implications
Why this matters for the field.

## Critical Assessment
Your informed take on quality, significance, and caveats.

## Community Reception
What's the discussion like? (web-search Twitter/X, Reddit, LessWrong, blog responses)
- Endorsements or criticism from notable researchers
- Citation count if paper is older than a few days
- If no discussion found yet, say so — that's also informative

## Key Terms
- **Term**: Definition in context of this paper.

## Related Papers
### [Paper Title](URL) (Year) — *Essential/Recommended/Optional*
Brief description.
*Why relevant: ...*
(2-4 related papers, web-verified, real papers only)
```

### Step 4: Write Output Files

1. **Individual paper files**: Save each analysis to `papers/YYYY-MM-DD_slugified-title.md`
2. **Update papers.json**: Append entries with this structure:
```json
{
  "id": "YYYY-MM-DD_slugified-title",
  "title": "Full Title",
  "authors": ["Author 1"],
  "url": "https://...",
  "doi": null,
  "source": "arxiv",
  "published_date": "YYYY-MM-DD",
  "fetched_date": "YYYY-MM-DD",
  "topics": ["mechanistic interpretability"],
  "relevance_score": 0.85,
  "confidence": "high",
  "version": "v1",
  "code_available": false,
  "triage": "read in full",
  "summary_file": "papers/YYYY-MM-DD_slugified-title.md",
  "related_paper_ids": []
}
```
3. **Daily report**: Save to `reports/YYYY-MM-DD.md` with format:

```markdown
# Literature Guide — YYYY-MM-DD

## Highlights
Top 3-5 most important items with brief context on why they matter.

## Papers

### [Paper Title](URL)
**Authors:** ... | **Source:** ... | **Relevance:** 0.XX | **Confidence:** HIGH/MED/LOW | **Triage:** Read in full / Skim / Awareness
**Published:** YYYY-MM-DD | **Version:** v1 or v2 (revised from ...) | **Code:** Yes/No
> Plain language summary (2-3 sentences)

**Key findings:**
- ...
- ...

**Why it matters:** One sentence on significance.

---
(repeat for each paper)

## Opportunities
### Jobs & Fellowships
- [Title](URL) — source

### Workshop CFPs & Events
- [Title](URL) — deadline if known

## Meta
- Sources checked: N
- Papers scanned: ~N
- Papers selected: N
- Report generated: YYYY-MM-DDTHH:MM:SSZ
```

### Step 5: Commit and Push

```bash
git add reports/ papers/ papers.json
git commit -m "daily digest: YYYY-MM-DD"
git push origin main
```

### Step 6: Send Email

Use Python's smtplib to send an HTML email via Gmail SMTP. Credentials are in environment variables:
- `SMTP_USER` — Gmail address
- `SMTP_PASSWORD` — Gmail app password
- `EMAIL_TO` — recipient (thomasjiralerspong@gmail.com)

The email should be a styled HTML digest with:
- Date header
- Highlights section (top 3-5 with links)
- Each paper: title (linked), authors, plain language summary, key findings, relevance score
- Opportunities section
- Footer with link to full report on GitHub

Use this Python snippet template:
```python
import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart('alternative')
msg['Subject'] = f'Literature Digest — {date}'
msg['From'] = os.environ['SMTP_USER']
msg['To'] = os.environ['EMAIL_TO']
msg.attach(MIMEText(html_content, 'html'))

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(os.environ['SMTP_USER'], os.environ['SMTP_PASSWORD'])
    server.sendmail(msg['From'], msg['To'], msg.as_string())
```

## Research Interests (for ranking)

**Core topics** (high relevance):
- Mechanistic interpretability
- AI safety & alignment
- Language model personas
- Emergent misalignment
- Subliminal learning
- Superposition / feature decomposition

**Always include** (regardless of topic match):
- Major papers from Anthropic, DeepMind, OpenAI, Meta AI, Google Brain
- Papers with >100 citations or significant community discussion
- Breakthrough results in any ML subfield

## Quality Standards

- NEVER fabricate paper titles, authors, or URLs — every paper must come from a real web search result
- NEVER guess author h-index or affiliations — web-search them
- Related papers must be web-verified real papers with real URLs
- If a search returns no results for a source, skip it — don't make things up
- Relevance scores: 0.9+ = directly in core topics by known researchers, 0.7-0.9 = relevant topic, 0.5-0.7 = adjacent/important, <0.5 = general interest landmark paper
