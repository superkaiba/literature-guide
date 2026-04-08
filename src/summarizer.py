from __future__ import annotations

import json
import logging
from datetime import date

import anthropic

from src.json_utils import extract_json
from src.models import RawPaper, SummarizedPaper, RelatedPaper, make_paper_id

log = logging.getLogger(__name__)

SUMMARIZE_PROMPT = """You are a research assistant for an ML researcher focused on: {topics}.

Analyze this paper thoroughly. Use web search to look up the authors and verify details.

Title: {title}
Authors: {authors}
Abstract: {abstract}
Source: {source}

Your tasks:
1. Search the web for each author to find their current affiliation, h-index, notable prior work, and research focus.
2. Search for any discussion of this paper (blog posts, Twitter/X threads, reviews).
3. Assess the paper's reliability based on what you find.

Return JSON:
{{
    "summary": "4-6 sentences providing a detailed summary. Describe the key contribution, methodology, main findings, and implications. Be specific about technical details.",
    "why_it_matters": "2-3 sentences explaining why this matters for the researcher's interests. Connect to broader trends.",
    "author_info": "2-4 sentences about the authors based on your web search. Include their current affiliations, notable prior work (with paper names), h-index or citation counts if found, and research focus areas.",
    "reliability_assessment": "2-3 sentences assessing credibility. Consider: author track record and citation counts, institutional affiliation, peer-review status vs preprint, methodology quality, whether claims are proportionate to evidence. Rate as HIGH/MEDIUM/LOW confidence with explanation.",
    "related_papers": [
        {{
            "title": "Exact title of a real, existing paper",
            "url": "URL if known, otherwise empty string",
            "year": 2024,
            "summary": "2-3 sentences summarizing this related paper and how it connects."
        }}
    ]
}}

Suggest 1-2 related papers. They must be REAL papers — verify via web search if unsure.
Return ONLY the JSON, no other text."""


def _extract_text_from_response(response) -> str:
    """Extract text content from a response that may contain thinking blocks."""
    for block in response.content:
        if block.type == "text":
            return block.text
    return ""


def summarize_paper(
    paper: RawPaper,
    topics: list[str],
    score: float,
    api_key: str,
    model: str = "claude-opus-4-6",
) -> SummarizedPaper:
    client = anthropic.Anthropic(api_key=api_key)
    today = date.today().isoformat()

    response = client.messages.create(
        model=model,
        max_tokens=16000,
        thinking={
            "type": "enabled",
            "budget_tokens": 10000,
        },
        tools=[
            {
                "name": "web_search",
                "type": "web_search_20250305",
            }
        ],
        messages=[
            {
                "role": "user",
                "content": SUMMARIZE_PROMPT.format(
                    topics=", ".join(topics),
                    title=paper.title,
                    authors=", ".join(paper.authors),
                    abstract=paper.abstract[:2000],
                    source=paper.source,
                ),
            }
        ],
    )

    raw_text = _extract_text_from_response(response)
    if not raw_text:
        log.warning("No text content in response for '%s'", paper.title)
        raw_text = "{}"

    data = json.loads(extract_json(raw_text))

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
        summary=data.get("summary", ""),
        why_it_matters=data.get("why_it_matters", ""),
        author_info=data.get("author_info", ""),
        reliability_assessment=data.get("reliability_assessment", ""),
        related_papers=related,
    )
