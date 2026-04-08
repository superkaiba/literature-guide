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

### Step 1b: Personalized Picks — scan VM for current work and find related older papers

Dispatch a subagent to:

1. **Scan recently modified files on the VM** to infer what the user is currently working on:
   ```bash
   # Find files modified in last 3 days (excluding hidden dirs, caches, venvs)
   find /home/thomasjiralerspong -maxdepth 4 -type f -mtime -3 \
     -not -path '*/.*' -not -path '*/node_modules/*' \
     -not -path '*/__pycache__/*' -not -path '*/venv/*' \
     -not -path '*/.venv/*' -not -path '*/lit_review/*' 2>/dev/null | head -60

   # Check recent git commits in all repos
   for d in /home/thomasjiralerspong/*/; do
     if [ -d "$d/.git" ]; then
       echo "=== $d ===";
       git -C "$d" log --oneline -10 2>/dev/null;
     fi
   done

   # Read READMEs, CLAUDE.md, research logs in active repos
   ```
   Read the most recently modified .py, .ipynb, .tex, .md files to understand
   the current research focus — what models, methods, datasets, and research
   questions are being actively worked on.

2. **Summarize the user's current work** in 3-5 sentences: what topic, what
   specific experiments, what methods, what models.

3. **Web-search for 3 older papers** (NOT from the last 2-3 days — could be
   from last week, last month, or even a classic from years ago) that are
   directly relevant to the user's current experiments. These should be papers
   the user might have missed or not thought to connect to their work — not
   the obvious ones they'd already know about. Search for:
   - Papers using similar methods on similar problems
   - Papers with findings that would inform the user's current experiments
   - Papers from adjacent fields that have relevant techniques or results
   
   For each paper, return: title, authors, URL, date, and a 3-4 sentence
   explanation of **why this specific paper matters for what the user is
   currently doing** (not a generic summary — connect it to their active work).

These 3 papers get added to the digest in a separate "Personalized Picks" section.
They use the same deep analysis format as other papers but with an additional
"**Connection to your current work:**" paragraph at the top explaining specifically
how the paper relates to what you're doing right now on this VM.

### Step 2: Deduplicate and Rank

From all search results, deduplicate by title similarity. Then select the top 10-20 papers using two criteria:
1. **Topic relevance** to core interests: mechanistic interpretability, AI safety, alignment, language model personas, emergent misalignment, subliminal learning, superposition features
2. **General importance** — landmark papers from Anthropic, DeepMind, OpenAI, Meta, Google Brain should ALWAYS be included even if outside core topics

### Step 3: Deep Analysis (use subagents in parallel)

For each selected paper, dispatch a subagent to produce a rich analysis. The subagent should:

1. **Web-search the paper URL** to read the abstract/full text
2. **Web-search each author** for affiliations, h-index, notable prior work
3. **Web-search for discussion** of the paper (Twitter/X, Reddit, blog posts)

Then produce this structured analysis. BE THOROUGH. Each section should be multiple
sentences or paragraphs. Include specific numbers, effect sizes, p-values, model names,
dataset sizes. Do NOT write vague one-liners — write like a knowledgeable reviewer who
has actually read the paper and is giving an honest, detailed assessment to a colleague.

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

## Phase 1: Initial Summary

### 1. Overview
What kind of paper this is (short empirical, full conference paper, theoretical, position paper,
blog post, etc.), who wrote it (lab/institution), where it's published or posted, and what
question it asks. 2-4 sentences.

### 2. Core Components

**Main Goal & Hypothesis.** What the authors set out to show, in specific terms. Not just
"they study X" but "they aim to show that Y causes Z, measured by W." Include the specific
framing/terminology they use.

**Key Findings.** 3-6 findings, each as a PARAGRAPH (not a one-liner). Include:
- Specific quantitative results (exact numbers, percentages, effect sizes, p-values)
- What comparison/baseline makes the number meaningful
- Whether the result is surprising or expected given prior work
- Any important caveats on that specific finding

**Methodology.** Detailed: which models (name, size), which datasets (name, size),
how many runs/seeds, what statistical tests, what hyperparameters matter. Someone
should be able to roughly assess the experimental design from this section alone.

**Distinctive Features.** What specifically sets this apart from the 2-3 most related
prior papers? Not "it's novel" but "unlike X (2024) which did Y, this paper does Z,
which matters because W."

**Limitations & Open Questions.** Two categories:
- *Authors' own stated limitations* — what they acknowledge
- *Obvious gaps the authors don't mention* — what YOU notice is missing
Be specific: "only 2 models" is less useful than "only Qwen2.5-7B and Llama-3.1-8B;
no frontier or closed models, which limits generalizability of the attack to models
with stronger safety training."

**Implications.** How this connects to broader research directions, threat models,
or practical deployment concerns. Include specific connections to other recent work
where relevant.

## Phase 2: Critical Assessment

### Conclusions vs. Evidence
Where are the paper's claims well-supported by data, and where do they oversell?
Be specific: "The X result is clean and well-controlled, but the Y claim relies on
an effect size of only Z%, which is tiny relative to the gap between [baseline] and
[ceiling]." Call out framing that goes beyond what the data show.

### Questionable Assumptions
Name them explicitly. What does the paper assume that might not hold? What would
break if the assumption fails? E.g., "System-prompt access to Agent0 is assumed;
whether the attack works through user-prompt-only access is untested and would be
a much more realistic threat model."

### Fit in Field
How does this sit relative to the broader research landscape? Is it a proof-of-concept,
a mature contribution, a "+MAS extension paper"? Who should care about it and why?
What's the natural follow-on work?

## Phase 3: Reference Material

### Confidence & Provenance
- **Confidence: HIGH/MEDIUM/LOW** — one-line rationale
- **Author credibility:** Senior author's h-index, top 2-3 prior papers, lab reputation
- **Venue/status:** Peer-reviewed (where?), preprint, blog post. If preprint, flag it.
- **Version:** First release, or revision? If revision, what changed? (web-search arXiv version history)
- **Code/data:** Released? Link if available. "No code" is a yellow flag for empirical papers.
- **Community reception:** Endorsements, criticism, or silence from notable researchers. Citation count if older than a few days.

### Triage Recommendation
**Read in full** / **Read abstract + key findings** / **Awareness only**
One sentence justifying the recommendation.

### Key Terms
Define 5-10 terms that a reader needs to understand this paper. Include technical
terms, statistical methods, and domain-specific jargon. Write actual definitions,
not just the term name. E.g.:
- **Mann-Whitney U test**: nonparametric test for whether two distributions differ;
  used here to compare response rates under subliminal vs. random tokens.

### Suggested Related Work
3-6 papers, each with:
- Full citation with URL (web-verified, real papers only)
- Priority tag: **Essential** / **Recommended** / **Optional**
- 2-3 sentences explaining WHY this specific paper is relevant — not a generic
  description of the paper, but how it connects to the paper under review.
  E.g.: "Direct predecessor; introduces subliminal prompting in single user-LLM
  settings and the entanglement token framing this paper builds on."
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

## Personalized Picks
Older papers (not from today's sources) related to what you're currently working on.

### [Paper Title](URL)
**Authors:** ... | **Source:** ... | **Published:** YYYY-MM-DD
**Connection to your current work:** 2-3 sentences explaining specifically how this
paper relates to the experiments/code you're actively running on this VM right now.

> Plain language summary (2-3 sentences)

**Key findings:**
- ...

**Why you should read this:** One sentence on what you'd get out of it.

---
(repeat for each personalized pick, typically 3 papers)

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
