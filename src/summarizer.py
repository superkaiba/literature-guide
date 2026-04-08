from __future__ import annotations

import json
from datetime import date

import anthropic

from src.json_utils import extract_json
from src.models import RawPaper, SummarizedPaper, RelatedPaper, make_paper_id

SUMMARIZE_PROMPT = """You are a research assistant for an ML researcher focused on: {topics}.

Summarize this paper, describe the authors, and suggest related work.

Title: {title}
Authors: {authors}
Abstract: {abstract}
Source: {source}

Return JSON:
{{
    "summary": "4-6 sentences providing a detailed summary of the paper. Describe the key contribution, methodology, main findings, and implications. Be specific about technical details.",
    "why_it_matters": "2-3 sentences explaining why this matters for the researcher's interests. Connect it to broader trends in the field.",
    "author_info": "1-3 sentences about who the authors are. Mention their affiliations (e.g. Anthropic, DeepMind, MIT), notable prior work, and research focus areas. If you don't recognize them, say so briefly.",
    "reliability_assessment": "1-3 sentences assessing how reliable/credible this paper is. Consider: author reputation and track record, institutional affiliation, whether it's peer-reviewed or a preprint, methodology quality based on the abstract, whether claims seem proportionate to evidence, and any red flags. Rate as HIGH/MEDIUM/LOW confidence with explanation.",
    "related_papers": [
        {{
            "title": "Exact title of a real, existing paper",
            "url": "URL if known, otherwise empty string",
            "year": 2024,
            "summary": "2-3 sentences summarizing this related paper and how it connects."
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
        max_tokens=2048,
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

    data = json.loads(extract_json(response.content[0].text))

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
        author_info=data.get("author_info", ""),
        reliability_assessment=data.get("reliability_assessment", ""),
        related_papers=related,
    )
