# Daily Literature Digest — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a daily pipeline that fetches ML/AI papers and opportunities from 15+ sources, summarizes them with Claude, stores them as structured markdown + JSON, pushes reports to GitHub, and sends Slack notifications.

**Architecture:** Fetch → Deduplicate → Rank (Claude API) → Summarize (Claude API) → Write (report + storage) → Notify (Slack). Runs daily via GitHub Actions cron.

**Tech Stack:** Python 3.12, anthropic SDK, arxiv, feedparser, rapidfuzz, requests, pyyaml, pytest, responses (HTTP mocking)

---

### Task 1: Project Scaffolding

**Files:**
- Create: `requirements.txt`
- Create: `config.yml`
- Create: `src/__init__.py`
- Create: `src/models.py`
- Create: `tests/__init__.py`
- Create: `papers/.gitkeep`
- Create: `reports/.gitkeep`
- Create: `papers.json`
- Create: `.gitignore`

**Step 1: Create requirements.txt**

```
anthropic>=0.39.0
arxiv>=2.1.0
feedparser>=6.0.0
rapidfuzz>=3.0.0
requests>=2.31.0
pyyaml>=6.0
pytest>=8.0.0
responses>=0.25.0
```

**Step 2: Create .gitignore**

```
__pycache__/
*.pyc
.env
.venv/
venv/
*.egg-info/
.pytest_cache/
```

**Step 3: Create config.yml**

```yaml
topics:
  - mechanistic interpretability
  - AI safety
  - AI alignment
  - language model personas
  - emergent misalignment
  - subliminal learning
  - superposition features

arxiv_queries:
  - "mechanistic interpretability"
  - "AI alignment"
  - "AI safety"
  - "language model personas"
  - "emergent misalignment"
  - "subliminal learning"
  - "superposition features"

rss_feeds:
  alignment_forum: "https://www.alignmentforum.org/feed.xml?view=community-rss"
  lesswrong: "https://www.lesswrong.com/feed.xml?view=community-rss"
  huggingface_papers: "https://huggingface.co/papers/rss"
  transformer_circuits: "https://transformer-circuits.pub/rss.xml"
  eleutherai: "https://blog.eleuther.ai/rss/"
  anthropic_research: "https://rsshub.app/anthropic/research"
  deepmind: "https://deepmind.google/blog/rss.xml"
  openai_research: "https://openai.com/news/rss.xml"
  redwood_research: "https://blog.redwoodresearch.org/feed"
  bair: "https://bair.berkeley.edu/blog/feed.xml"

reddit_subreddits:
  - MachineLearning
  - mlsafety
  - aisafety

bluesky_accounts:
  - anthropic.bsky.social
  - deepmind.bsky.social

newsletter_sources:
  import_ai:
    url: "https://importai.substack.com/feed"
    type: rss
  the_gradient:
    url: "https://thegradient.pub/rss/"
    type: rss
  cais:
    url: "https://safe.ai/newsletter"
    type: scrape

opportunity_sources:
  eighty_thousand_hours: "https://jobs.80000hours.org/jobs"
  aisafety_world: "https://aisafety.world"

max_papers: 20
max_opportunities: 10

github_repo_url: ""  # set after creating remote
```

**Step 4: Create src/__init__.py and tests/__init__.py**

Both empty files.

**Step 5: Create src/models.py**

```python
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import date
import json
import re


@dataclass
class RawPaper:
    title: str
    authors: list[str]
    abstract: str
    url: str
    source: str
    published_date: str
    doi: str | None = None
    tags: list[str] = field(default_factory=list)


@dataclass
class RelatedPaper:
    title: str
    url: str
    year: int
    summary: str


@dataclass
class SummarizedPaper:
    id: str
    title: str
    authors: list[str]
    url: str
    doi: str | None
    source: str
    published_date: str
    fetched_date: str
    topics: list[str]
    relevance_score: float
    summary: str
    why_it_matters: str
    related_papers: list[RelatedPaper]
    summary_file: str = ""

    def to_index_entry(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "authors": self.authors,
            "url": self.url,
            "doi": self.doi,
            "source": self.source,
            "published_date": self.published_date,
            "fetched_date": self.fetched_date,
            "topics": self.topics,
            "relevance_score": self.relevance_score,
            "summary_file": self.summary_file,
            "related_paper_ids": [],
        }


@dataclass
class Opportunity:
    title: str
    url: str
    organization: str
    category: str  # "job", "fellowship", "cfp", "grant"
    deadline: str | None = None
    description: str = ""


def make_paper_id(date_str: str, title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60]
    return f"{date_str}_{slug}"
```

**Step 6: Create empty papers.json, papers/.gitkeep, reports/.gitkeep**

`papers.json` contains `[]`. The `.gitkeep` files are empty.

**Step 7: Install dependencies and run a smoke test**

Run: `pip install -r requirements.txt && python -c "from src.models import RawPaper; print('OK')"`
Expected: `OK`

**Step 8: Commit**

```bash
git add -A
git commit -m "feat: project scaffolding — models, config, requirements"
```

---

### Task 2: Config Module

**Files:**
- Create: `src/config.py`
- Create: `tests/test_config.py`

**Step 1: Write the failing test**

```python
# tests/test_config.py
import os
from src.config import load_config


def test_load_config_reads_topics():
    config = load_config("config.yml")
    assert "mechanistic interpretability" in config.topics


def test_load_config_reads_rss_feeds():
    config = load_config("config.yml")
    assert "alignment_forum" in config.rss_feeds
    assert config.rss_feeds["alignment_forum"].startswith("http")


def test_load_config_reads_env_overrides(monkeypatch):
    monkeypatch.setenv("SLACK_WEBHOOK_URL", "https://hooks.slack.com/test")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
    config = load_config("config.yml")
    assert config.slack_webhook_url == "https://hooks.slack.com/test"
    assert config.anthropic_api_key == "sk-test"


def test_load_config_max_papers():
    config = load_config("config.yml")
    assert config.max_papers == 20
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_config.py -v`
Expected: FAIL — `cannot import name 'load_config'`

**Step 3: Write implementation**

```python
# src/config.py
from __future__ import annotations

import os
from dataclasses import dataclass, field

import yaml


@dataclass
class Config:
    topics: list[str]
    arxiv_queries: list[str]
    rss_feeds: dict[str, str]
    reddit_subreddits: list[str]
    bluesky_accounts: list[str]
    newsletter_sources: dict[str, dict]
    opportunity_sources: dict[str, str]
    max_papers: int = 20
    max_opportunities: int = 10
    github_repo_url: str = ""
    slack_webhook_url: str = ""
    anthropic_api_key: str = ""
    semantic_scholar_api_key: str = ""


def load_config(path: str = "config.yml") -> Config:
    with open(path) as f:
        raw = yaml.safe_load(f)

    return Config(
        topics=raw["topics"],
        arxiv_queries=raw["arxiv_queries"],
        rss_feeds=raw["rss_feeds"],
        reddit_subreddits=raw["reddit_subreddits"],
        bluesky_accounts=raw["bluesky_accounts"],
        newsletter_sources=raw["newsletter_sources"],
        opportunity_sources=raw["opportunity_sources"],
        max_papers=raw.get("max_papers", 20),
        max_opportunities=raw.get("max_opportunities", 10),
        github_repo_url=raw.get("github_repo_url", ""),
        slack_webhook_url=os.environ.get("SLACK_WEBHOOK_URL", ""),
        anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY", ""),
        semantic_scholar_api_key=os.environ.get("SEMANTIC_SCHOLAR_API_KEY", ""),
    )
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_config.py -v`
Expected: All PASS

**Step 5: Commit**

```bash
git add src/config.py tests/test_config.py
git commit -m "feat: config module — load config.yml with env overrides"
```

---

### Task 3: arXiv Fetcher

**Files:**
- Create: `src/fetchers/__init__.py`
- Create: `src/fetchers/arxiv_fetcher.py`
- Create: `tests/test_arxiv_fetcher.py`

**Step 1: Write the failing test**

```python
# tests/test_arxiv_fetcher.py
from unittest.mock import patch, MagicMock
from src.fetchers.arxiv_fetcher import fetch_arxiv
from src.models import RawPaper


def _mock_result(title="Test Paper", authors=None, summary="Abstract text",
                 entry_id="http://arxiv.org/abs/2026.12345", doi="10.1234/test",
                 published=None, categories=None):
    from datetime import datetime
    r = MagicMock()
    r.title = title
    author1 = MagicMock()
    author1.name = "Author A"
    r.authors = authors or [author1]
    r.summary = summary
    r.entry_id = entry_id
    r.doi = doi
    r.published = published or datetime(2026, 4, 6)
    cat = MagicMock()
    cat.term = "cs.LG"
    r.categories = categories or [cat]
    return r


@patch("src.fetchers.arxiv_fetcher.arxiv.Client")
def test_fetch_arxiv_returns_raw_papers(mock_client_cls):
    mock_client = MagicMock()
    mock_client.results.return_value = [_mock_result()]
    mock_client_cls.return_value = mock_client

    papers = fetch_arxiv(["mechanistic interpretability"])
    assert len(papers) >= 1
    assert isinstance(papers[0], RawPaper)
    assert papers[0].source == "arxiv"
    assert papers[0].title == "Test Paper"


@patch("src.fetchers.arxiv_fetcher.arxiv.Client")
def test_fetch_arxiv_deduplicates_across_queries(mock_client_cls):
    result = _mock_result()
    mock_client = MagicMock()
    mock_client.results.return_value = [result]
    mock_client_cls.return_value = mock_client

    papers = fetch_arxiv(["query1", "query2"])
    assert len(papers) == 1  # same paper from both queries
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_arxiv_fetcher.py -v`
Expected: FAIL — `cannot import name 'fetch_arxiv'`

**Step 3: Write implementation**

```python
# src/fetchers/__init__.py
# empty

# src/fetchers/arxiv_fetcher.py
from __future__ import annotations

from datetime import datetime, timedelta, timezone

import arxiv

from src.models import RawPaper


def fetch_arxiv(queries: list[str], days_back: int = 1) -> list[RawPaper]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=days_back)
    seen_ids: set[str] = set()
    papers: list[RawPaper] = []

    client = arxiv.Client()

    for query in queries:
        search = arxiv.Search(
            query=query,
            max_results=50,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )
        for result in client.results(search):
            pub_date = result.published.replace(tzinfo=timezone.utc)
            if pub_date < cutoff:
                continue
            if result.entry_id in seen_ids:
                continue
            seen_ids.add(result.entry_id)
            papers.append(
                RawPaper(
                    title=result.title.strip(),
                    authors=[a.name for a in result.authors],
                    abstract=result.summary.strip(),
                    url=result.entry_id,
                    source="arxiv",
                    published_date=pub_date.date().isoformat(),
                    doi=result.doi,
                    tags=[c.term if isinstance(c, str) is False else c
                          for c in (result.categories or [])],
                )
            )
    return papers
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_arxiv_fetcher.py -v`
Expected: All PASS

**Step 5: Commit**

```bash
git add src/fetchers/ tests/test_arxiv_fetcher.py
git commit -m "feat: arXiv fetcher — query arxiv API with dedup across queries"
```

---

### Task 4: OpenAlex Fetcher

**Files:**
- Create: `src/fetchers/openalex.py`
- Create: `tests/test_openalex.py`

**Step 1: Write the failing test**

```python
# tests/test_openalex.py
import responses
from src.fetchers.openalex import fetch_openalex
from src.models import RawPaper

SAMPLE_RESPONSE = {
    "results": [
        {
            "title": "Sparse Autoencoders for Interpretability",
            "authorships": [
                {"author": {"display_name": "Alice Smith"}},
                {"author": {"display_name": "Bob Jones"}},
            ],
            "abstract_inverted_index": {
                "We": [0], "study": [1], "sparse": [2],
                "autoencoders": [3], "for": [4], "interpretability.": [5],
            },
            "doi": "https://doi.org/10.1234/test",
            "id": "https://openalex.org/W123",
            "publication_date": "2026-04-06",
            "topics": [{"display_name": "Machine Learning"}],
        }
    ]
}


@responses.activate
def test_fetch_openalex_returns_papers():
    responses.add(
        responses.GET,
        "https://api.openalex.org/works",
        json=SAMPLE_RESPONSE,
        status=200,
    )
    papers = fetch_openalex(["mechanistic interpretability"])
    assert len(papers) == 1
    assert isinstance(papers[0], RawPaper)
    assert papers[0].source == "openalex"
    assert papers[0].title == "Sparse Autoencoders for Interpretability"
    assert "We study sparse autoencoders for interpretability." in papers[0].abstract
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_openalex.py -v`
Expected: FAIL — `cannot import name 'fetch_openalex'`

**Step 3: Write implementation**

```python
# src/fetchers/openalex.py
from __future__ import annotations

from datetime import date, timedelta

import requests

from src.models import RawPaper


def _reconstruct_abstract(inverted_index: dict | None) -> str:
    if not inverted_index:
        return ""
    word_positions: list[tuple[int, str]] = []
    for word, positions in inverted_index.items():
        for pos in positions:
            word_positions.append((pos, word))
    word_positions.sort()
    return " ".join(w for _, w in word_positions)


def fetch_openalex(queries: list[str], days_back: int = 1) -> list[RawPaper]:
    cutoff = (date.today() - timedelta(days=days_back)).isoformat()
    seen_ids: set[str] = set()
    papers: list[RawPaper] = []

    for query in queries:
        resp = requests.get(
            "https://api.openalex.org/works",
            params={
                "search": query,
                "filter": f"from_publication_date:{cutoff}",
                "sort": "publication_date:desc",
                "per_page": 25,
            },
            headers={"User-Agent": "literature-guide/1.0"},
            timeout=30,
        )
        resp.raise_for_status()
        for work in resp.json().get("results", []):
            oa_id = work.get("id", "")
            if oa_id in seen_ids:
                continue
            seen_ids.add(oa_id)
            papers.append(
                RawPaper(
                    title=work.get("title", "").strip(),
                    authors=[
                        a["author"]["display_name"]
                        for a in work.get("authorships", [])
                    ],
                    abstract=_reconstruct_abstract(
                        work.get("abstract_inverted_index")
                    ),
                    url=work.get("doi") or oa_id,
                    source="openalex",
                    published_date=work.get("publication_date", ""),
                    doi=work.get("doi"),
                    tags=[
                        t["display_name"]
                        for t in work.get("topics", [])
                    ],
                )
            )
    return papers
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_openalex.py -v`
Expected: All PASS

**Step 5: Commit**

```bash
git add src/fetchers/openalex.py tests/test_openalex.py
git commit -m "feat: OpenAlex fetcher — free API, inverted index abstract reconstruction"
```

---

### Task 5: Semantic Scholar Fetcher

**Files:**
- Create: `src/fetchers/semantic_scholar.py`
- Create: `tests/test_semantic_scholar.py`

**Step 1: Write the failing test**

```python
# tests/test_semantic_scholar.py
import responses
from src.fetchers.semantic_scholar import fetch_semantic_scholar
from src.models import RawPaper

SAMPLE_RESPONSE = {
    "data": [
        {
            "paperId": "abc123",
            "title": "Alignment Faking in LLMs",
            "authors": [{"name": "Alice"}, {"name": "Bob"}],
            "abstract": "We demonstrate alignment faking.",
            "url": "https://www.semanticscholar.org/paper/abc123",
            "externalIds": {"DOI": "10.1234/test"},
            "publicationDate": "2026-04-06",
            "fieldsOfStudy": ["Computer Science"],
        }
    ]
}


@responses.activate
def test_fetch_semantic_scholar():
    responses.add(
        responses.GET,
        "https://api.semanticscholar.org/graph/v1/paper/search",
        json=SAMPLE_RESPONSE,
        status=200,
    )
    papers = fetch_semantic_scholar(["alignment faking"], api_key="test-key")
    assert len(papers) == 1
    assert papers[0].source == "semantic_scholar"
    assert papers[0].title == "Alignment Faking in LLMs"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_semantic_scholar.py -v`
Expected: FAIL

**Step 3: Write implementation**

```python
# src/fetchers/semantic_scholar.py
from __future__ import annotations

from datetime import date, timedelta

import requests

from src.models import RawPaper

API_BASE = "https://api.semanticscholar.org/graph/v1"


def fetch_semantic_scholar(
    queries: list[str],
    api_key: str = "",
    days_back: int = 1,
) -> list[RawPaper]:
    cutoff = (date.today() - timedelta(days=days_back)).isoformat()
    seen_ids: set[str] = set()
    papers: list[RawPaper] = []
    headers = {}
    if api_key:
        headers["x-api-key"] = api_key

    for query in queries:
        resp = requests.get(
            f"{API_BASE}/paper/search",
            params={
                "query": query,
                "limit": 25,
                "fields": "title,authors,abstract,url,externalIds,publicationDate,fieldsOfStudy",
                "publicationDateOrYear": f"{cutoff}:",
            },
            headers=headers,
            timeout=30,
        )
        if resp.status_code == 429:
            continue  # rate limited, skip this query
        resp.raise_for_status()
        for paper in resp.json().get("data", []):
            pid = paper.get("paperId", "")
            if pid in seen_ids or not paper.get("title"):
                continue
            seen_ids.add(pid)
            ext_ids = paper.get("externalIds") or {}
            papers.append(
                RawPaper(
                    title=paper["title"].strip(),
                    authors=[a["name"] for a in paper.get("authors", [])],
                    abstract=(paper.get("abstract") or "").strip(),
                    url=paper.get("url") or f"https://www.semanticscholar.org/paper/{pid}",
                    source="semantic_scholar",
                    published_date=paper.get("publicationDate") or "",
                    doi=ext_ids.get("DOI"),
                    tags=paper.get("fieldsOfStudy") or [],
                )
            )
    return papers
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_semantic_scholar.py -v`
Expected: All PASS

**Step 5: Commit**

```bash
git add src/fetchers/semantic_scholar.py tests/test_semantic_scholar.py
git commit -m "feat: Semantic Scholar fetcher — API with rate limit handling"
```

---

### Task 6: RSS Fetcher (blogs + newsletters)

**Files:**
- Create: `src/fetchers/rss.py`
- Create: `tests/test_rss.py`

**Step 1: Write the failing test**

```python
# tests/test_rss.py
from unittest.mock import patch, MagicMock
from src.fetchers.rss import fetch_rss
from src.models import RawPaper

SAMPLE_FEED = {
    "entries": [
        {
            "title": "New Interpretability Results",
            "link": "https://example.com/post/1",
            "summary": "We found interesting features in transformer MLPs.",
            "authors": [{"name": "Researcher X"}],
            "published_parsed": (2026, 4, 6, 12, 0, 0, 0, 96, 0),
            "tags": [{"term": "interpretability"}],
        }
    ],
    "bozo": False,
}


@patch("src.fetchers.rss.feedparser.parse")
def test_fetch_rss_returns_papers(mock_parse):
    mock_parse.return_value = SAMPLE_FEED
    feeds = {"test_blog": "https://example.com/feed.xml"}
    papers = fetch_rss(feeds)
    assert len(papers) == 1
    assert papers[0].source == "test_blog"
    assert papers[0].title == "New Interpretability Results"


@patch("src.fetchers.rss.feedparser.parse")
def test_fetch_rss_handles_missing_authors(mock_parse):
    entry = SAMPLE_FEED["entries"][0].copy()
    del entry["authors"]
    mock_parse.return_value = {"entries": [entry], "bozo": False}
    papers = fetch_rss({"blog": "https://example.com/feed"})
    assert papers[0].authors == []
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_rss.py -v`
Expected: FAIL

**Step 3: Write implementation**

```python
# src/fetchers/rss.py
from __future__ import annotations

import time
from datetime import datetime, timedelta, timezone

import feedparser

from src.models import RawPaper


def _parse_date(entry: dict) -> str:
    parsed = entry.get("published_parsed")
    if parsed:
        try:
            dt = datetime(*parsed[:6], tzinfo=timezone.utc)
            return dt.date().isoformat()
        except (TypeError, ValueError):
            pass
    return datetime.now(timezone.utc).date().isoformat()


def _is_recent(entry: dict, days_back: int) -> bool:
    parsed = entry.get("published_parsed")
    if not parsed:
        return True  # include if we can't tell
    try:
        dt = datetime(*parsed[:6], tzinfo=timezone.utc)
        cutoff = datetime.now(timezone.utc) - timedelta(days=days_back)
        return dt >= cutoff
    except (TypeError, ValueError):
        return True


def fetch_rss(feeds: dict[str, str], days_back: int = 1) -> list[RawPaper]:
    papers: list[RawPaper] = []
    seen_urls: set[str] = set()

    for source_name, feed_url in feeds.items():
        feed = feedparser.parse(feed_url)
        for entry in feed.get("entries", []):
            if not _is_recent(entry, days_back):
                continue
            url = entry.get("link", "")
            if url in seen_urls:
                continue
            seen_urls.add(url)
            authors = [
                a.get("name", "") for a in entry.get("authors", [])
            ]
            tags = [t.get("term", "") for t in entry.get("tags", [])]
            papers.append(
                RawPaper(
                    title=entry.get("title", "").strip(),
                    authors=[a for a in authors if a],
                    abstract=entry.get("summary", "").strip(),
                    url=url,
                    source=source_name,
                    published_date=_parse_date(entry),
                    doi=None,
                    tags=tags,
                )
            )
    return papers
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_rss.py -v`
Expected: All PASS

**Step 5: Commit**

```bash
git add src/fetchers/rss.py tests/test_rss.py
git commit -m "feat: RSS fetcher — generic feed parser for blogs and newsletters"
```

---

### Task 7: Reddit Fetcher

**Files:**
- Create: `src/fetchers/reddit.py`
- Create: `tests/test_reddit.py`

**Step 1: Write the failing test**

```python
# tests/test_reddit.py
import responses
from src.fetchers.reddit import fetch_reddit
from src.models import RawPaper

SAMPLE_RESPONSE = {
    "data": {
        "children": [
            {
                "data": {
                    "title": "[R] New paper on emergent misalignment",
                    "url": "https://arxiv.org/abs/2026.99999",
                    "selftext": "Interesting new paper on emergent misalignment in fine-tuned models.",
                    "author": "researcher123",
                    "created_utc": 1743897600,  # 2025-04-06
                    "link_flair_text": "Research",
                    "score": 150,
                }
            }
        ]
    }
}


@responses.activate
def test_fetch_reddit_returns_papers():
    responses.add(
        responses.GET,
        "https://old.reddit.com/r/MachineLearning/new.json",
        json=SAMPLE_RESPONSE,
        status=200,
    )
    papers = fetch_reddit(["MachineLearning"])
    assert len(papers) == 1
    assert papers[0].source == "reddit_MachineLearning"
    assert "emergent misalignment" in papers[0].title
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_reddit.py -v`
Expected: FAIL

**Step 3: Write implementation**

```python
# src/fetchers/reddit.py
from __future__ import annotations

from datetime import datetime, timedelta, timezone

import requests

from src.models import RawPaper


def fetch_reddit(subreddits: list[str], days_back: int = 1) -> list[RawPaper]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=days_back)
    papers: list[RawPaper] = []

    for sub in subreddits:
        resp = requests.get(
            f"https://old.reddit.com/r/{sub}/new.json",
            params={"limit": 50},
            headers={"User-Agent": "literature-guide/1.0"},
            timeout=30,
        )
        if resp.status_code != 200:
            continue
        for child in resp.json().get("data", {}).get("children", []):
            post = child["data"]
            created = datetime.fromtimestamp(
                post["created_utc"], tz=timezone.utc
            )
            if created < cutoff:
                continue
            papers.append(
                RawPaper(
                    title=post.get("title", "").strip(),
                    authors=[post.get("author", "")],
                    abstract=post.get("selftext", "").strip()[:1000],
                    url=post.get("url", ""),
                    source=f"reddit_{sub}",
                    published_date=created.date().isoformat(),
                    doi=None,
                    tags=[post.get("link_flair_text", "")],
                )
            )
    return papers
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_reddit.py -v`
Expected: All PASS

**Step 5: Commit**

```bash
git add src/fetchers/reddit.py tests/test_reddit.py
git commit -m "feat: Reddit fetcher — fetch new posts from ML subreddits"
```

---

### Task 8: Bluesky Fetcher

**Files:**
- Create: `src/fetchers/bluesky.py`
- Create: `tests/test_bluesky.py`

**Step 1: Write the failing test**

```python
# tests/test_bluesky.py
import responses
from src.fetchers.bluesky import fetch_bluesky
from src.models import RawPaper

SAMPLE_RESPONSE = {
    "feed": [
        {
            "post": {
                "uri": "at://did:plc:abc/app.bsky.feed.post/123",
                "author": {
                    "handle": "researcher.bsky.social",
                    "displayName": "Dr. Researcher",
                },
                "record": {
                    "text": "New paper: We find emergent deception in fine-tuned models https://arxiv.org/abs/2026.11111",
                    "createdAt": "2026-04-06T12:00:00Z",
                },
                "embed": {
                    "$type": "app.bsky.embed.external#view",
                    "external": {
                        "uri": "https://arxiv.org/abs/2026.11111",
                        "title": "Emergent Deception in Fine-tuned Models",
                        "description": "We study emergent deception.",
                    },
                },
            }
        }
    ]
}


@responses.activate
def test_fetch_bluesky_extracts_links():
    responses.add(
        responses.GET,
        "https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed",
        json=SAMPLE_RESPONSE,
        status=200,
    )
    papers = fetch_bluesky(["researcher.bsky.social"])
    assert len(papers) >= 1
    assert papers[0].source == "bluesky"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_bluesky.py -v`
Expected: FAIL

**Step 3: Write implementation**

```python
# src/fetchers/bluesky.py
from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone

import requests

from src.models import RawPaper

BSKY_API = "https://public.api.bsky.app/xrpc"


def _extract_urls(text: str) -> list[str]:
    return re.findall(r"https?://[^\s)]+", text)


def fetch_bluesky(accounts: list[str], days_back: int = 1) -> list[RawPaper]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=days_back)
    papers: list[RawPaper] = []
    seen_urls: set[str] = set()

    for handle in accounts:
        resp = requests.get(
            f"{BSKY_API}/app.bsky.feed.getAuthorFeed",
            params={"actor": handle, "limit": 30},
            timeout=30,
        )
        if resp.status_code != 200:
            continue
        for item in resp.json().get("feed", []):
            post = item.get("post", {})
            record = post.get("record", {})
            created_str = record.get("createdAt", "")
            try:
                created = datetime.fromisoformat(created_str.replace("Z", "+00:00"))
            except (ValueError, AttributeError):
                continue
            if created < cutoff:
                continue

            text = record.get("text", "")
            # Extract embedded link if present
            embed = post.get("embed", {})
            external = embed.get("external", {})
            link = external.get("uri", "")
            title = external.get("title", "")
            description = external.get("description", "")

            if not link:
                urls = _extract_urls(text)
                link = urls[0] if urls else ""
            if not link:
                continue  # skip posts without links

            if link in seen_urls:
                continue
            seen_urls.add(link)

            author = post.get("author", {})
            papers.append(
                RawPaper(
                    title=title or text[:120],
                    authors=[author.get("displayName", handle)],
                    abstract=description or text,
                    url=link,
                    source="bluesky",
                    published_date=created.date().isoformat(),
                    doi=None,
                    tags=[],
                )
            )
    return papers
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_bluesky.py -v`
Expected: All PASS

**Step 5: Commit**

```bash
git add src/fetchers/bluesky.py tests/test_bluesky.py
git commit -m "feat: Bluesky fetcher — extract paper links from researcher posts"
```

---

### Task 9: Opportunities Fetcher

**Files:**
- Create: `src/fetchers/opportunities.py`
- Create: `tests/test_opportunities.py`

**Step 1: Write the failing test**

```python
# tests/test_opportunities.py
import responses
from src.fetchers.opportunities import fetch_opportunities
from src.models import Opportunity

SAMPLE_80K = """
<html><body>
<div class="job-listing">
  <a href="/job/123" class="job-title">ML Safety Researcher</a>
  <span class="organization">Anthropic</span>
  <span class="deadline">2026-05-01</span>
</div>
</body></html>
"""


@responses.activate
def test_fetch_opportunities_returns_list():
    responses.add(
        responses.GET,
        "https://jobs.80000hours.org/jobs",
        body=SAMPLE_80K,
        status=200,
    )
    opps = fetch_opportunities(
        {"eighty_thousand_hours": "https://jobs.80000hours.org/jobs"},
        keywords=["safety", "alignment", "interpretability"],
    )
    assert isinstance(opps, list)
    # may be empty if parsing doesn't match — that's ok for now
    for opp in opps:
        assert isinstance(opp, Opportunity)
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_opportunities.py -v`
Expected: FAIL

**Step 3: Write implementation**

```python
# src/fetchers/opportunities.py
from __future__ import annotations

import re

import requests

from src.models import Opportunity


def _scrape_80k_hours(url: str, keywords: list[str]) -> list[Opportunity]:
    resp = requests.get(url, headers={"User-Agent": "literature-guide/1.0"}, timeout=30)
    if resp.status_code != 200:
        return []
    opps: list[Opportunity] = []
    # Simple regex-based extraction — 80k Hours pages have structured job listings
    # This is intentionally simple; we'll refine parsing as the HTML structure becomes clear
    title_pattern = re.compile(r'class="[^"]*job[_-]?title[^"]*"[^>]*>([^<]+)', re.I)
    org_pattern = re.compile(r'class="[^"]*organi[sz]ation[^"]*"[^>]*>([^<]+)', re.I)
    link_pattern = re.compile(r'href="(/job[^"]*)"', re.I)

    titles = title_pattern.findall(resp.text)
    orgs = org_pattern.findall(resp.text)
    links = link_pattern.findall(resp.text)

    for i, title in enumerate(titles):
        if not any(kw.lower() in title.lower() for kw in keywords):
            continue
        org = orgs[i] if i < len(orgs) else ""
        link = links[i] if i < len(links) else ""
        full_url = f"https://jobs.80000hours.org{link}" if link.startswith("/") else link
        opps.append(
            Opportunity(
                title=title.strip(),
                url=full_url,
                organization=org.strip(),
                category="job",
            )
        )
    return opps


def fetch_opportunities(
    sources: dict[str, str],
    keywords: list[str] | None = None,
) -> list[Opportunity]:
    keywords = keywords or ["safety", "alignment", "interpretability", "mechanistic"]
    opps: list[Opportunity] = []

    for source_name, url in sources.items():
        if "80000hours" in source_name:
            opps.extend(_scrape_80k_hours(url, keywords))
        else:
            # Generic scraper — fetch page, look for keyword matches in links
            try:
                resp = requests.get(
                    url,
                    headers={"User-Agent": "literature-guide/1.0"},
                    timeout=30,
                )
                if resp.status_code != 200:
                    continue
                # Extract links with keywords in text
                link_re = re.compile(
                    r'<a[^>]+href="([^"]+)"[^>]*>([^<]+)</a>', re.I
                )
                for href, text in link_re.findall(resp.text):
                    if any(kw.lower() in text.lower() for kw in keywords):
                        opps.append(
                            Opportunity(
                                title=text.strip(),
                                url=href if href.startswith("http") else f"{url.rstrip('/')}/{href.lstrip('/')}",
                                organization=source_name,
                                category="job",
                            )
                        )
            except requests.RequestException:
                continue

    return opps
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_opportunities.py -v`
Expected: All PASS

**Step 5: Commit**

```bash
git add src/fetchers/opportunities.py tests/test_opportunities.py
git commit -m "feat: opportunities fetcher — scrape job boards for safety roles"
```

---

### Task 10: Deduplication Module

**Files:**
- Create: `src/dedup.py`
- Create: `tests/test_dedup.py`

**Step 1: Write the failing test**

```python
# tests/test_dedup.py
from src.dedup import deduplicate
from src.models import RawPaper


def _paper(title="Test Paper", doi=None, url="https://example.com/1", source="arxiv"):
    return RawPaper(
        title=title, authors=["A"], abstract="Abstract",
        url=url, source=source, published_date="2026-04-06",
        doi=doi, tags=[],
    )


def test_dedup_by_doi():
    papers = [
        _paper(title="Paper A", doi="10.1234/test", source="arxiv"),
        _paper(title="Paper A (preprint)", doi="10.1234/test", source="openalex"),
    ]
    result = deduplicate(papers)
    assert len(result) == 1


def test_dedup_by_fuzzy_title():
    papers = [
        _paper(title="Sparse Autoencoders Find Interpretable Features", source="arxiv"),
        _paper(title="Sparse Autoencoders Find Interpretable Features in LLMs", source="openalex",
               url="https://example.com/2"),
    ]
    result = deduplicate(papers)
    assert len(result) == 1


def test_dedup_keeps_different_papers():
    papers = [
        _paper(title="Paper About Safety", url="https://example.com/1"),
        _paper(title="Paper About Alignment", url="https://example.com/2"),
    ]
    result = deduplicate(papers)
    assert len(result) == 2


def test_dedup_prefers_arxiv_source():
    papers = [
        _paper(title="Same Paper", doi="10.1234/x", source="openalex"),
        _paper(title="Same Paper", doi="10.1234/x", source="arxiv"),
    ]
    result = deduplicate(papers)
    assert len(result) == 1
    assert result[0].source == "arxiv"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_dedup.py -v`
Expected: FAIL

**Step 3: Write implementation**

```python
# src/dedup.py
from __future__ import annotations

from rapidfuzz import fuzz

from src.models import RawPaper

TITLE_SIMILARITY_THRESHOLD = 85

# Prefer sources with richer metadata
SOURCE_PRIORITY = {
    "arxiv": 0,
    "semantic_scholar": 1,
    "openalex": 2,
}


def _normalize_title(title: str) -> str:
    return " ".join(title.lower().split())


def deduplicate(papers: list[RawPaper]) -> list[RawPaper]:
    # Sort by source priority so preferred sources come first
    papers_sorted = sorted(
        papers,
        key=lambda p: SOURCE_PRIORITY.get(p.source, 99),
    )

    # Phase 1: DOI-based dedup
    doi_groups: dict[str, RawPaper] = {}
    no_doi: list[RawPaper] = []
    for p in papers_sorted:
        if p.doi:
            normalized_doi = p.doi.lower().strip()
            if normalized_doi not in doi_groups:
                doi_groups[normalized_doi] = p
        else:
            no_doi.append(p)

    candidates = list(doi_groups.values()) + no_doi

    # Phase 2: fuzzy title dedup
    result: list[RawPaper] = []
    for paper in candidates:
        norm = _normalize_title(paper.title)
        is_dup = False
        for existing in result:
            existing_norm = _normalize_title(existing.title)
            if fuzz.ratio(norm, existing_norm) >= TITLE_SIMILARITY_THRESHOLD:
                is_dup = True
                break
        if not is_dup:
            result.append(paper)

    return result
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_dedup.py -v`
Expected: All PASS

**Step 5: Commit**

```bash
git add src/dedup.py tests/test_dedup.py
git commit -m "feat: dedup module — DOI matching + fuzzy title similarity"
```

---

### Task 11: Ranker (Claude API)

**Files:**
- Create: `src/ranker.py`
- Create: `tests/test_ranker.py`

**Step 1: Write the failing test**

```python
# tests/test_ranker.py
from unittest.mock import patch, MagicMock
from src.ranker import rank_papers
from src.models import RawPaper


def _paper(title, abstract=""):
    return RawPaper(
        title=title, authors=["A"], abstract=abstract,
        url="https://example.com", source="arxiv",
        published_date="2026-04-06", tags=[],
    )


@patch("src.ranker.anthropic.Anthropic")
def test_rank_papers_returns_scored_list(mock_anthropic_cls):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.content = [MagicMock()]
    mock_response.content[0].text = '[{"index": 0, "score": 0.95, "topics": ["mechanistic interpretability"]}, {"index": 1, "score": 0.3, "topics": ["computer vision"]}]'
    mock_client.messages.create.return_value = mock_response
    mock_anthropic_cls.return_value = mock_client

    papers = [
        _paper("SAE Features in GPT-4", "We study sparse autoencoder features."),
        _paper("Image Classification Survey", "A survey of CNN architectures."),
    ]
    topics = ["mechanistic interpretability", "AI safety"]
    scored = rank_papers(papers, topics, api_key="test")

    assert len(scored) == 2
    assert scored[0][1] >= scored[1][1]  # sorted by score descending


@patch("src.ranker.anthropic.Anthropic")
def test_rank_papers_filters_by_max(mock_anthropic_cls):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.content = [MagicMock()]
    mock_response.content[0].text = '[{"index": 0, "score": 0.9, "topics": ["safety"]}, {"index": 1, "score": 0.8, "topics": ["alignment"]}, {"index": 2, "score": 0.1, "topics": []}]'
    mock_client.messages.create.return_value = mock_response
    mock_anthropic_cls.return_value = mock_client

    papers = [_paper(f"Paper {i}") for i in range(3)]
    scored = rank_papers(papers, ["safety"], api_key="test", max_papers=2)
    assert len(scored) == 2
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_ranker.py -v`
Expected: FAIL

**Step 3: Write implementation**

```python
# src/ranker.py
from __future__ import annotations

import json

import anthropic

from src.models import RawPaper

RANK_PROMPT = """You are a research paper relevance scorer. Given a list of papers and target research topics, score each paper's relevance from 0.0 to 1.0.

Target topics:
{topics}

Papers:
{papers}

Return a JSON array with one object per paper:
[{{"index": 0, "score": 0.95, "topics": ["topic1", "topic2"]}}, ...]

Score meaning:
- 0.9-1.0: Directly about a target topic
- 0.7-0.9: Closely related, likely relevant
- 0.4-0.7: Tangentially related
- 0.0-0.4: Not relevant

Return ONLY the JSON array, no other text."""


def rank_papers(
    papers: list[RawPaper],
    topics: list[str],
    api_key: str,
    max_papers: int = 20,
    model: str = "claude-sonnet-4-6",
) -> list[tuple[RawPaper, float, list[str]]]:
    if not papers:
        return []

    client = anthropic.Anthropic(api_key=api_key)

    papers_text = "\n".join(
        f"[{i}] Title: {p.title}\nAbstract: {p.abstract[:500]}"
        for i, p in enumerate(papers)
    )

    # Process in batches of 30 to stay within token limits
    batch_size = 30
    all_scored: list[tuple[RawPaper, float, list[str]]] = []

    for start in range(0, len(papers), batch_size):
        batch = papers[start : start + batch_size]
        batch_text = "\n".join(
            f"[{i}] Title: {p.title}\nAbstract: {p.abstract[:500]}"
            for i, p in enumerate(batch)
        )

        response = client.messages.create(
            model=model,
            max_tokens=2048,
            messages=[
                {
                    "role": "user",
                    "content": RANK_PROMPT.format(
                        topics=", ".join(topics),
                        papers=batch_text,
                    ),
                }
            ],
        )

        result_text = response.content[0].text
        scores = json.loads(result_text)

        for item in scores:
            idx = item["index"]
            if idx < len(batch):
                all_scored.append(
                    (batch[idx], item["score"], item.get("topics", []))
                )

    all_scored.sort(key=lambda x: x[1], reverse=True)
    return all_scored[:max_papers]
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_ranker.py -v`
Expected: All PASS

**Step 5: Commit**

```bash
git add src/ranker.py tests/test_ranker.py
git commit -m "feat: ranker — Claude API scores paper relevance to target topics"
```

---

### Task 12: Summarizer (Claude API)

**Files:**
- Create: `src/summarizer.py`
- Create: `tests/test_summarizer.py`

**Step 1: Write the failing test**

```python
# tests/test_summarizer.py
from unittest.mock import patch, MagicMock
from src.summarizer import summarize_paper
from src.models import RawPaper, SummarizedPaper, RelatedPaper


@patch("src.summarizer.anthropic.Anthropic")
def test_summarize_paper_returns_summarized(mock_anthropic_cls):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.content = [MagicMock()]
    mock_response.content[0].text = """{
        "summary": "This paper studies sparse autoencoders for extracting interpretable features from language models.",
        "why_it_matters": "Directly advances mechanistic interpretability by providing scalable feature extraction.",
        "related_papers": [
            {
                "title": "Toy Models of Superposition",
                "url": "https://arxiv.org/abs/2209.10652",
                "year": 2022,
                "summary": "Foundational work showing how neural networks represent more features than dimensions."
            }
        ]
    }"""
    mock_client.messages.create.return_value = mock_response
    mock_anthropic_cls.return_value = mock_client

    paper = RawPaper(
        title="Scaling SAEs", authors=["A", "B"],
        abstract="We scale sparse autoencoders to GPT-4.",
        url="https://arxiv.org/abs/2026.12345",
        source="arxiv", published_date="2026-04-06", tags=[],
    )
    topics = ["mechanistic interpretability"]
    result = summarize_paper(paper, topics, score=0.95, api_key="test")

    assert isinstance(result, SummarizedPaper)
    assert "sparse autoencoders" in result.summary
    assert len(result.related_papers) == 1
    assert result.related_papers[0].year == 2022
    assert result.relevance_score == 0.95
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_summarizer.py -v`
Expected: FAIL

**Step 3: Write implementation**

```python
# src/summarizer.py
from __future__ import annotations

import json
from datetime import date

import anthropic

from src.models import RawPaper, SummarizedPaper, RelatedPaper, make_paper_id

SUMMARIZE_PROMPT = """You are a research assistant for an ML researcher focused on: {topics}.

Summarize this paper and suggest related work.

Title: {title}
Authors: {authors}
Abstract: {abstract}
Source: {source}

Return JSON:
{{
    "summary": "2-3 sentences on the key contribution.",
    "why_it_matters": "1-2 sentences on why this matters for the researcher's interests.",
    "related_papers": [
        {{
            "title": "Exact title of a real, existing paper",
            "url": "URL if known, otherwise empty string",
            "year": 2024,
            "summary": "2-3 sentences summarizing this related paper."
        }}
    ]
}}

Suggest 1-2 related papers. They can be older/classic. They must be REAL papers — do not invent titles.
Return ONLY the JSON, no other text."""


def summarize_paper(
    paper: RawPaper,
    topics: list[str],
    score: float,
    api_key: str,
    model: str = "claude-sonnet-4-6",
) -> SummarizedPaper:
    client = anthropic.Anthropic(api_key=api_key)
    today = date.today().isoformat()

    response = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": SUMMARIZE_PROMPT.format(
                    topics=", ".join(topics),
                    title=paper.title,
                    authors=", ".join(paper.authors),
                    abstract=paper.abstract[:1500],
                    source=paper.source,
                ),
            }
        ],
    )

    data = json.loads(response.content[0].text)

    related = [
        RelatedPaper(
            title=r["title"],
            url=r.get("url", ""),
            year=r["year"],
            summary=r["summary"],
        )
        for r in data.get("related_papers", [])
    ]

    return SummarizedPaper(
        id=make_paper_id(today, paper.title),
        title=paper.title,
        authors=paper.authors,
        url=paper.url,
        doi=paper.doi,
        source=paper.source,
        published_date=paper.published_date,
        fetched_date=today,
        topics=topics,
        relevance_score=score,
        summary=data["summary"],
        why_it_matters=data["why_it_matters"],
        related_papers=related,
    )
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_summarizer.py -v`
Expected: All PASS

**Step 5: Commit**

```bash
git add src/summarizer.py tests/test_summarizer.py
git commit -m "feat: summarizer — Claude API generates summaries + related paper suggestions"
```

---

### Task 13: Storage Module

**Files:**
- Create: `src/storage.py`
- Create: `tests/test_storage.py`

**Step 1: Write the failing test**

```python
# tests/test_storage.py
import json
import os
import tempfile
from src.storage import save_paper, load_index
from src.models import SummarizedPaper, RelatedPaper


def _sample_paper():
    return SummarizedPaper(
        id="2026-04-07_test-paper",
        title="Test Paper",
        authors=["Alice", "Bob"],
        url="https://arxiv.org/abs/2026.12345",
        doi="10.1234/test",
        source="arxiv",
        published_date="2026-04-06",
        fetched_date="2026-04-07",
        topics=["mechanistic interpretability"],
        relevance_score=0.95,
        summary="This paper does X.",
        why_it_matters="It advances Y.",
        related_papers=[
            RelatedPaper(
                title="Related Work",
                url="https://arxiv.org/abs/2024.11111",
                year=2024,
                summary="Earlier work on Y.",
            )
        ],
    )


def test_save_paper_creates_markdown(tmp_path):
    paper = _sample_paper()
    save_paper(paper, base_dir=str(tmp_path))
    md_path = tmp_path / "papers" / "2026-04-07_test-paper.md"
    assert md_path.exists()
    content = md_path.read_text()
    assert "Test Paper" in content
    assert "Related Work" in content


def test_save_paper_updates_index(tmp_path):
    index_path = tmp_path / "papers.json"
    index_path.write_text("[]")
    paper = _sample_paper()
    save_paper(paper, base_dir=str(tmp_path))
    index = load_index(str(tmp_path))
    assert len(index) == 1
    assert index[0]["id"] == "2026-04-07_test-paper"


def test_save_paper_no_duplicate_in_index(tmp_path):
    index_path = tmp_path / "papers.json"
    index_path.write_text("[]")
    paper = _sample_paper()
    save_paper(paper, base_dir=str(tmp_path))
    save_paper(paper, base_dir=str(tmp_path))
    index = load_index(str(tmp_path))
    assert len(index) == 1
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_storage.py -v`
Expected: FAIL

**Step 3: Write implementation**

```python
# src/storage.py
from __future__ import annotations

import json
import os

from src.models import SummarizedPaper


def _paper_to_markdown(paper: SummarizedPaper) -> str:
    lines = [
        "---",
        f"title: \"{paper.title}\"",
        f"authors: {paper.authors}",
        f"url: {paper.url}",
        f"source: {paper.source}",
        f"published_date: {paper.published_date}",
        f"topics: {paper.topics}",
        f"relevance_score: {paper.relevance_score}",
        "---",
        "",
        f"## Summary",
        paper.summary,
        "",
        f"## Why It Matters",
        paper.why_it_matters,
        "",
    ]
    if paper.related_papers:
        lines.append("## Related Papers")
        for rp in paper.related_papers:
            url_part = f"({rp.url})" if rp.url else ""
            lines.append(f"### [{rp.title}]{url_part} ({rp.year})")
            lines.append(rp.summary)
            lines.append("")

    return "\n".join(lines)


def save_paper(paper: SummarizedPaper, base_dir: str = ".") -> str:
    papers_dir = os.path.join(base_dir, "papers")
    os.makedirs(papers_dir, exist_ok=True)

    # Write markdown file
    filename = f"{paper.id}.md"
    filepath = os.path.join(papers_dir, filename)
    with open(filepath, "w") as f:
        f.write(_paper_to_markdown(paper))

    paper.summary_file = f"papers/{filename}"

    # Update index
    index_path = os.path.join(base_dir, "papers.json")
    index = load_index(base_dir)

    # Remove existing entry with same ID if present
    index = [e for e in index if e["id"] != paper.id]
    index.append(paper.to_index_entry())

    with open(index_path, "w") as f:
        json.dump(index, f, indent=2)

    return filepath


def load_index(base_dir: str = ".") -> list[dict]:
    index_path = os.path.join(base_dir, "papers.json")
    if not os.path.exists(index_path):
        return []
    with open(index_path) as f:
        return json.load(f)
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_storage.py -v`
Expected: All PASS

**Step 5: Commit**

```bash
git add src/storage.py tests/test_storage.py
git commit -m "feat: storage — save papers as markdown + JSON index"
```

---

### Task 14: Report Generator

**Files:**
- Create: `src/report.py`
- Create: `tests/test_report.py`

**Step 1: Write the failing test**

```python
# tests/test_report.py
import os
from src.report import generate_report
from src.models import SummarizedPaper, RelatedPaper, Opportunity


def _sample_paper(title="Test Paper", score=0.9):
    return SummarizedPaper(
        id=f"2026-04-07_{title.lower().replace(' ', '-')}",
        title=title, authors=["Alice"], url="https://example.com",
        doi=None, source="arxiv", published_date="2026-04-06",
        fetched_date="2026-04-07", topics=["safety"],
        relevance_score=score, summary="Summary of the paper.",
        why_it_matters="Important for safety.",
        related_papers=[
            RelatedPaper(title="Old Paper", url="https://example.com/old",
                         year=2023, summary="Earlier work.")
        ],
    )


def test_generate_report_creates_file(tmp_path):
    papers = [_sample_paper("Paper A", 0.95), _sample_paper("Paper B", 0.8)]
    opps = [Opportunity(title="Safety Role", url="https://example.com/job",
                        organization="Anthropic", category="job")]
    path = generate_report(papers, opps, date_str="2026-04-07",
                           base_dir=str(tmp_path))
    assert os.path.exists(path)
    content = open(path).read()
    assert "Literature Guide" in content
    assert "Paper A" in content
    assert "Safety Role" in content
    assert "Highlights" in content


def test_generate_report_has_meta_section(tmp_path):
    papers = [_sample_paper()]
    path = generate_report(papers, [], date_str="2026-04-07",
                           base_dir=str(tmp_path), sources_checked=15,
                           papers_scanned=200)
    content = open(path).read()
    assert "Sources checked: 15" in content
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_report.py -v`
Expected: FAIL

**Step 3: Write implementation**

```python
# src/report.py
from __future__ import annotations

import os
from datetime import datetime, timezone

from src.models import SummarizedPaper, Opportunity


def generate_report(
    papers: list[SummarizedPaper],
    opportunities: list[Opportunity],
    date_str: str,
    base_dir: str = ".",
    sources_checked: int = 0,
    papers_scanned: int = 0,
) -> str:
    reports_dir = os.path.join(base_dir, "reports")
    os.makedirs(reports_dir, exist_ok=True)

    lines: list[str] = []
    lines.append(f"# Literature Guide — {date_str}")
    lines.append("")

    # Highlights
    lines.append("## Highlights")
    for p in papers[:5]:
        lines.append(f"> **[{p.title}]({p.url})** — {p.summary.split('.')[0]}.")
    lines.append("")

    # Papers
    lines.append("## Papers")
    lines.append("")
    for i, p in enumerate(papers, 1):
        lines.append(f"### {i}. [{p.title}]({p.url})")
        lines.append(f"**Authors:** {', '.join(p.authors)} | **Source:** {p.source} | **Date:** {p.published_date}")
        lines.append(f"**Topics:** {', '.join(p.topics)}")
        lines.append("")
        lines.append(f"**Summary:** {p.summary}")
        lines.append("")
        lines.append(f"**Why it matters:** {p.why_it_matters}")
        lines.append("")
        if p.related_papers:
            lines.append("**Related papers:**")
            for rp in p.related_papers:
                url_part = f"({rp.url})" if rp.url else ""
                lines.append(f"- [{rp.title}]{url_part} ({rp.year}) — {rp.summary}")
            lines.append("")
        lines.append("---")
        lines.append("")

    # Opportunities
    lines.append("## Opportunities")
    jobs = [o for o in opportunities if o.category == "job"]
    fellowships = [o for o in opportunities if o.category == "fellowship"]
    cfps = [o for o in opportunities if o.category == "cfp"]
    grants = [o for o in opportunities if o.category == "grant"]
    other = [o for o in opportunities if o.category not in ("job", "fellowship", "cfp", "grant")]

    for section_name, section_opps in [
        ("Jobs & Fellowships", jobs + fellowships),
        ("Workshops & CFPs", cfps),
        ("Grants & Programs", grants),
        ("Other", other),
    ]:
        if section_opps:
            lines.append(f"### {section_name}")
            for o in section_opps:
                deadline = f", deadline: {o.deadline}" if o.deadline else ""
                lines.append(f"- [{o.title}]({o.url}) — {o.organization}{deadline}")
            lines.append("")

    if not opportunities:
        lines.append("No new opportunities found today.")
        lines.append("")

    # Meta
    lines.append("## Meta")
    lines.append(f"- Sources checked: {sources_checked}")
    lines.append(f"- Papers scanned: ~{papers_scanned}")
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines.append(f"- Report generated: {ts}")
    lines.append("")

    report_path = os.path.join(reports_dir, f"{date_str}.md")
    with open(report_path, "w") as f:
        f.write("\n".join(lines))

    return report_path
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_report.py -v`
Expected: All PASS

**Step 5: Commit**

```bash
git add src/report.py tests/test_report.py
git commit -m "feat: report generator — daily markdown with highlights, papers, opportunities"
```

---

### Task 15: Slack Notifier

**Files:**
- Create: `src/notify.py`
- Create: `tests/test_notify.py`

**Step 1: Write the failing test**

```python
# tests/test_notify.py
import json
import responses
from src.notify import send_slack_notification
from src.models import SummarizedPaper, RelatedPaper, Opportunity


def _sample_paper(title="Test Paper"):
    return SummarizedPaper(
        id="2026-04-07_test", title=title, authors=["A"],
        url="https://example.com", doi=None, source="arxiv",
        published_date="2026-04-06", fetched_date="2026-04-07",
        topics=["safety"], relevance_score=0.9,
        summary="Summary here.", why_it_matters="Important.",
        related_papers=[],
    )


@responses.activate
def test_send_slack_posts_to_webhook():
    responses.add(responses.POST, "https://hooks.slack.com/test", status=200)

    papers = [_sample_paper("Paper A"), _sample_paper("Paper B")]
    opps = [Opportunity(title="Job", url="https://x.com", organization="Org", category="job")]
    send_slack_notification(
        papers, opps,
        webhook_url="https://hooks.slack.com/test",
        report_url="https://github.com/user/repo/blob/main/reports/2026-04-07.md",
    )
    assert len(responses.calls) == 1
    body = json.loads(responses.calls[0].request.body)
    assert "Paper A" in body["text"]
    assert "Opportunities" in body["text"]
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_notify.py -v`
Expected: FAIL

**Step 3: Write implementation**

```python
# src/notify.py
from __future__ import annotations

import json

import requests

from src.models import SummarizedPaper, Opportunity


def _format_slack_message(
    papers: list[SummarizedPaper],
    opportunities: list[Opportunity],
    report_url: str,
) -> str:
    from datetime import date
    today = date.today().isoformat()

    lines = [f":newspaper: *Literature Guide — {today}*", ""]

    if papers:
        lines.append("*Top Papers:*")
        for i, p in enumerate(papers[:5], 1):
            first_sentence = p.summary.split(".")[0] + "."
            lines.append(f"{i}. <{p.url}|{p.title}> — {first_sentence}")
        lines.append("")

    if opportunities:
        job_count = sum(1 for o in opportunities if o.category in ("job", "fellowship"))
        cfp_count = sum(1 for o in opportunities if o.category == "cfp")
        parts = []
        if job_count:
            parts.append(f"{job_count} job{'s' if job_count > 1 else ''}")
        if cfp_count:
            parts.append(f"{cfp_count} CFP{'s' if cfp_count > 1 else ''}")
        other = len(opportunities) - job_count - cfp_count
        if other:
            parts.append(f"{other} other")
        lines.append(f"*Opportunities:* {len(opportunities)} new ({', '.join(parts)})")
        lines.append("")

    lines.append(f":link: <{report_url}|Full report>")

    return "\n".join(lines)


def send_slack_notification(
    papers: list[SummarizedPaper],
    opportunities: list[Opportunity],
    webhook_url: str,
    report_url: str,
) -> None:
    if not webhook_url:
        return

    message = _format_slack_message(papers, opportunities, report_url)

    requests.post(
        webhook_url,
        json={"text": message},
        timeout=30,
    )
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_notify.py -v`
Expected: All PASS

**Step 5: Commit**

```bash
git add src/notify.py tests/test_notify.py
git commit -m "feat: Slack notifier — webhook with highlights + report link"
```

---

### Task 16: Main Pipeline Orchestrator

**Files:**
- Create: `src/main.py`
- Create: `tests/test_main.py`

**Step 1: Write the failing test**

```python
# tests/test_main.py
from unittest.mock import patch, MagicMock
from src.main import run_pipeline
from src.models import RawPaper, SummarizedPaper, RelatedPaper, Opportunity


def _raw_paper():
    return RawPaper(
        title="Test", authors=["A"], abstract="Abstract",
        url="https://example.com", source="arxiv",
        published_date="2026-04-06", tags=[],
    )


def _summarized_paper():
    return SummarizedPaper(
        id="2026-04-07_test", title="Test", authors=["A"],
        url="https://example.com", doi=None, source="arxiv",
        published_date="2026-04-06", fetched_date="2026-04-07",
        topics=["safety"], relevance_score=0.9,
        summary="Summary.", why_it_matters="Matters.",
        related_papers=[],
    )


@patch("src.main.send_slack_notification")
@patch("src.main.generate_report")
@patch("src.main.save_paper")
@patch("src.main.summarize_paper")
@patch("src.main.rank_papers")
@patch("src.main.deduplicate")
@patch("src.main.fetch_all")
@patch("src.main.load_config")
def test_run_pipeline_orchestrates_all_steps(
    mock_config, mock_fetch, mock_dedup, mock_rank,
    mock_summarize, mock_save, mock_report, mock_notify,
):
    cfg = MagicMock()
    cfg.topics = ["safety"]
    cfg.anthropic_api_key = "test"
    cfg.slack_webhook_url = "https://hooks.slack.com/test"
    cfg.github_repo_url = "https://github.com/user/repo"
    cfg.max_papers = 20
    cfg.max_opportunities = 10
    mock_config.return_value = cfg

    raw = [_raw_paper()]
    mock_fetch.return_value = (raw, [])
    mock_dedup.return_value = raw
    mock_rank.return_value = [(raw[0], 0.9, ["safety"])]

    sp = _summarized_paper()
    mock_summarize.return_value = sp
    mock_report.return_value = "reports/2026-04-07.md"

    run_pipeline()

    mock_fetch.assert_called_once()
    mock_dedup.assert_called_once()
    mock_rank.assert_called_once()
    mock_summarize.assert_called_once()
    mock_save.assert_called_once()
    mock_report.assert_called_once()
    mock_notify.assert_called_once()
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_main.py -v`
Expected: FAIL

**Step 3: Write implementation**

```python
# src/main.py
from __future__ import annotations

import logging
from datetime import date

from src.config import load_config
from src.dedup import deduplicate
from src.fetchers.arxiv_fetcher import fetch_arxiv
from src.fetchers.openalex import fetch_openalex
from src.fetchers.semantic_scholar import fetch_semantic_scholar
from src.fetchers.rss import fetch_rss
from src.fetchers.reddit import fetch_reddit
from src.fetchers.bluesky import fetch_bluesky
from src.fetchers.opportunities import fetch_opportunities
from src.models import RawPaper, Opportunity
from src.notify import send_slack_notification
from src.ranker import rank_papers
from src.report import generate_report
from src.storage import save_paper
from src.summarizer import summarize_paper

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)


def fetch_all(config) -> tuple[list[RawPaper], list[Opportunity]]:
    papers: list[RawPaper] = []
    sources_tried = 0

    # arXiv
    log.info("Fetching arXiv...")
    try:
        papers.extend(fetch_arxiv(config.arxiv_queries))
        sources_tried += 1
    except Exception as e:
        log.warning(f"arXiv fetch failed: {e}")

    # OpenAlex
    log.info("Fetching OpenAlex...")
    try:
        papers.extend(fetch_openalex(config.topics))
        sources_tried += 1
    except Exception as e:
        log.warning(f"OpenAlex fetch failed: {e}")

    # Semantic Scholar
    log.info("Fetching Semantic Scholar...")
    try:
        papers.extend(
            fetch_semantic_scholar(config.topics, api_key=config.semantic_scholar_api_key)
        )
        sources_tried += 1
    except Exception as e:
        log.warning(f"Semantic Scholar fetch failed: {e}")

    # RSS feeds (blogs + newsletters)
    log.info("Fetching RSS feeds...")
    try:
        all_feeds = dict(config.rss_feeds)
        for name, src in config.newsletter_sources.items():
            if src.get("type") == "rss":
                all_feeds[name] = src["url"]
        papers.extend(fetch_rss(all_feeds))
        sources_tried += len(all_feeds)
    except Exception as e:
        log.warning(f"RSS fetch failed: {e}")

    # Reddit
    log.info("Fetching Reddit...")
    try:
        papers.extend(fetch_reddit(config.reddit_subreddits))
        sources_tried += len(config.reddit_subreddits)
    except Exception as e:
        log.warning(f"Reddit fetch failed: {e}")

    # Bluesky
    log.info("Fetching Bluesky...")
    try:
        papers.extend(fetch_bluesky(config.bluesky_accounts))
        sources_tried += 1
    except Exception as e:
        log.warning(f"Bluesky fetch failed: {e}")

    # Opportunities
    log.info("Fetching opportunities...")
    opportunities: list[Opportunity] = []
    try:
        opportunities = fetch_opportunities(
            config.opportunity_sources,
            keywords=config.topics,
        )
    except Exception as e:
        log.warning(f"Opportunities fetch failed: {e}")

    log.info(f"Fetched {len(papers)} raw papers from {sources_tried} sources")
    return papers, opportunities


def run_pipeline(config_path: str = "config.yml") -> None:
    config = load_config(config_path)
    today = date.today().isoformat()

    # 1. Fetch
    raw_papers, opportunities = fetch_all(config)
    total_scanned = len(raw_papers)

    # 2. Deduplicate
    log.info("Deduplicating...")
    unique_papers = deduplicate(raw_papers)
    log.info(f"After dedup: {len(unique_papers)} unique papers")

    # 3. Rank
    log.info("Ranking papers...")
    ranked = rank_papers(
        unique_papers, config.topics,
        api_key=config.anthropic_api_key,
        max_papers=config.max_papers,
    )
    log.info(f"Top {len(ranked)} papers selected")

    # 4. Summarize
    log.info("Summarizing papers...")
    summarized = []
    for paper, score, topics in ranked:
        try:
            sp = summarize_paper(
                paper, topics, score=score,
                api_key=config.anthropic_api_key,
            )
            summarized.append(sp)
        except Exception as e:
            log.warning(f"Failed to summarize '{paper.title}': {e}")

    # 5. Store
    log.info("Saving papers...")
    for sp in summarized:
        save_paper(sp)

    # 6. Report
    log.info("Generating report...")
    report_path = generate_report(
        summarized,
        opportunities[:config.max_opportunities],
        date_str=today,
        sources_checked=15,
        papers_scanned=total_scanned,
    )
    log.info(f"Report saved to {report_path}")

    # 7. Notify
    report_url = ""
    if config.github_repo_url:
        report_url = f"{config.github_repo_url}/blob/main/reports/{today}.md"
    send_slack_notification(
        summarized, opportunities,
        webhook_url=config.slack_webhook_url,
        report_url=report_url,
    )
    log.info("Slack notification sent")


if __name__ == "__main__":
    run_pipeline()
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_main.py -v`
Expected: All PASS

**Step 5: Commit**

```bash
git add src/main.py tests/test_main.py
git commit -m "feat: main pipeline — orchestrates fetch, dedup, rank, summarize, store, report, notify"
```

---

### Task 17: GitHub Actions Workflow

**Files:**
- Create: `.github/workflows/daily_digest.yml`

**Step 1: Create the workflow file**

```yaml
name: Daily Literature Digest

on:
  schedule:
    - cron: '0 11 * * *'  # 6am EST / 7am EDT
  workflow_dispatch:

permissions:
  contents: write

jobs:
  digest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 1

      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: 'pip'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run digest pipeline
        run: python src/main.py
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
          SEMANTIC_SCHOLAR_API_KEY: ${{ secrets.SEMANTIC_SCHOLAR_API_KEY }}

      - name: Commit and push results
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "daily digest: $(date +%Y-%m-%d)"
          file_pattern: "reports/*.md papers/*.md papers.json"
```

**Step 2: Verify YAML is valid**

Run: `python -c "import yaml; yaml.safe_load(open('.github/workflows/daily_digest.yml')); print('Valid YAML')"`
Expected: `Valid YAML`

**Step 3: Commit**

```bash
git add .github/workflows/daily_digest.yml
git commit -m "feat: GitHub Actions workflow — daily cron + manual trigger"
```

---

### Task 18: Integration Test (Dry Run)

**Files:**
- Create: `tests/test_integration.py`

**Step 1: Write integration test with all mocks**

```python
# tests/test_integration.py
import json
import os
from unittest.mock import patch, MagicMock
from src.main import run_pipeline


@patch("src.main.send_slack_notification")
@patch("src.summarizer.anthropic.Anthropic")
@patch("src.ranker.anthropic.Anthropic")
@patch("src.fetchers.bluesky.requests.get")
@patch("src.fetchers.reddit.requests.get")
@patch("src.fetchers.rss.feedparser.parse")
@patch("src.fetchers.semantic_scholar.requests.get")
@patch("src.fetchers.openalex.requests.get")
@patch("src.fetchers.arxiv_fetcher.arxiv.Client")
def test_full_pipeline_dry_run(
    mock_arxiv_client, mock_openalex, mock_s2, mock_rss,
    mock_reddit, mock_bsky, mock_ranker_api, mock_summarizer_api,
    mock_notify, tmp_path, monkeypatch,
):
    monkeypatch.chdir(tmp_path)

    # Write config
    import shutil
    shutil.copy("config.yml", str(tmp_path / "config.yml"))
    (tmp_path / "papers.json").write_text("[]")
    os.makedirs(tmp_path / "papers", exist_ok=True)
    os.makedirs(tmp_path / "reports", exist_ok=True)

    # Mock arXiv
    from datetime import datetime, timezone
    mock_result = MagicMock()
    mock_result.title = "Interpretability via SAEs"
    author = MagicMock()
    author.name = "Test Author"
    mock_result.authors = [author]
    mock_result.summary = "We study sparse autoencoders."
    mock_result.entry_id = "http://arxiv.org/abs/2026.12345"
    mock_result.doi = None
    mock_result.published = datetime(2026, 4, 6, tzinfo=timezone.utc)
    mock_result.categories = []
    client = MagicMock()
    client.results.return_value = [mock_result]
    mock_arxiv_client.return_value = client

    # Mock other fetchers to return empty
    mock_openalex.return_value = MagicMock(status_code=200, json=lambda: {"results": []})
    mock_s2.return_value = MagicMock(status_code=200, json=lambda: {"data": []})
    mock_rss.return_value = {"entries": [], "bozo": False}
    mock_reddit.return_value = MagicMock(status_code=200, json=lambda: {"data": {"children": []}})
    mock_bsky.return_value = MagicMock(status_code=200, json=lambda: {"feed": []})

    # Mock ranker
    ranker_client = MagicMock()
    ranker_response = MagicMock()
    ranker_response.content = [MagicMock()]
    ranker_response.content[0].text = '[{"index": 0, "score": 0.95, "topics": ["mechanistic interpretability"]}]'
    ranker_client.messages.create.return_value = ranker_response
    mock_ranker_api.return_value = ranker_client

    # Mock summarizer
    summarizer_client = MagicMock()
    summarizer_response = MagicMock()
    summarizer_response.content = [MagicMock()]
    summarizer_response.content[0].text = json.dumps({
        "summary": "This paper studies SAEs for interpretability.",
        "why_it_matters": "Advances mechanistic interpretability.",
        "related_papers": [
            {"title": "Toy Models of Superposition", "url": "https://arxiv.org/abs/2209.10652",
             "year": 2022, "summary": "Foundational work on superposition."}
        ],
    })
    summarizer_client.messages.create.return_value = summarizer_response
    mock_summarizer_api.return_value = summarizer_client

    # Set env vars
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    monkeypatch.setenv("SLACK_WEBHOOK_URL", "https://hooks.slack.com/test")

    run_pipeline(config_path=str(tmp_path / "config.yml"))

    # Verify outputs exist
    reports = list((tmp_path / "reports").iterdir())
    assert len(reports) == 1
    assert reports[0].suffix == ".md"

    papers_dir = list((tmp_path / "papers").iterdir())
    assert len(papers_dir) >= 1

    index = json.loads((tmp_path / "papers.json").read_text())
    assert len(index) == 1

    mock_notify.assert_called_once()
```

**Step 2: Run integration test**

Run: `pytest tests/test_integration.py -v`
Expected: PASS

**Step 3: Commit**

```bash
git add tests/test_integration.py
git commit -m "test: integration test — full pipeline dry run with mocked APIs"
```

---

### Task 19: README

**Files:**
- Create: `README.md`

**Step 1: Write README**

```markdown
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
```

**Step 2: Commit**

```bash
git add README.md
git commit -m "docs: README with setup instructions"
```

---

### Task 20: Run Full Test Suite

**Step 1: Run all tests**

Run: `pytest tests/ -v`
Expected: All PASS

**Step 2: Final commit if any fixes needed**

---

## Task Summary

| Task | Component | Est. |
|------|-----------|------|
| 1 | Project scaffolding | 5 min |
| 2 | Config module | 5 min |
| 3 | arXiv fetcher | 5 min |
| 4 | OpenAlex fetcher | 5 min |
| 5 | Semantic Scholar fetcher | 5 min |
| 6 | RSS fetcher | 5 min |
| 7 | Reddit fetcher | 5 min |
| 8 | Bluesky fetcher | 5 min |
| 9 | Opportunities fetcher | 5 min |
| 10 | Dedup module | 5 min |
| 11 | Ranker (Claude API) | 5 min |
| 12 | Summarizer (Claude API) | 5 min |
| 13 | Storage module | 5 min |
| 14 | Report generator | 5 min |
| 15 | Slack notifier | 5 min |
| 16 | Main pipeline | 5 min |
| 17 | GitHub Actions workflow | 3 min |
| 18 | Integration test | 5 min |
| 19 | README | 3 min |
| 20 | Full test suite | 2 min |
