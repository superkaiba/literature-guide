from __future__ import annotations

from dataclasses import dataclass, field
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
    priority: str = ""  # "Essential", "Recommended", "Optional"
    relevance: str = ""  # why it's relevant


@dataclass
class KeyTerm:
    term: str
    definition: str


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
    # Core analysis
    document_type: str  # "research paper", "blog post", "review", etc.
    overview: str  # 2-3 sentence overview
    main_goal: str  # primary objective in plain language
    key_findings: list[str]  # 3-5 most important results/claims
    methodology: str  # how the research was conducted
    distinctive_features: str  # what makes this unique
    limitations: str  # weaknesses and open questions
    implications: str  # why it matters, practical/theoretical consequences
    critical_assessment: str  # are conclusions well-supported?
    # Author and reliability
    author_info: str
    reliability_assessment: str
    # Terms and related work
    key_terms: list[KeyTerm]
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
