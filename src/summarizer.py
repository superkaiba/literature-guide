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

Suggest 1-2 related papers. They can be older/classic. They must be REAL papers.
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
