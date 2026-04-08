from __future__ import annotations

import json
import logging
import time
from datetime import date

import anthropic

from src.json_utils import extract_json
from src.models import RawPaper, SummarizedPaper, RelatedPaper, KeyTerm, make_paper_id

log = logging.getLogger(__name__)

SUMMARIZE_PROMPT = """You are an expert academic paper reviewer and research analyst.

## About the researcher you're writing for
They are an ML researcher focused on mechanistic interpretability, AI safety, alignment, language model personas, and weird generalization phenomena (emergent misalignment, subliminal learning, superposition). They also want to stay broadly current with important ML/AI developments. Their specific interests include: {topics}.

## Your task
Thoroughly analyze this paper. Use web search to look up the authors, verify claims, and find related discussions. Tailor the "implications" section to explain how this connects to the researcher's interests — even for papers outside their core topics, explain why it matters for the broader field they operate in.

Title: {title}
Authors: {authors}
Abstract: {abstract}
Source: {source}

## Your Tasks

1. **Search the web** for each author — find their current affiliation, h-index, notable prior work, and research focus.
2. **Search for discussion** of this paper — blog posts, Twitter/X threads, conference reviews, Reddit threads.
3. **Identify related work** — search for the most important papers this builds on or competes with.
4. **Assess reliability** based on everything you find.

## Return JSON with this structure:

{{
    "document_type": "research paper | blog post | review | commentary | preprint",
    "plain_language_summary": "3-5 sentences explaining what this paper does and why it matters as if talking to a smart friend who isn't a specialist. No jargon, no acronyms. Use analogies and intuitions. Start with the 'so what' — why should anyone care? Then explain the key idea and result in everyday terms.",
    "overview": "2-3 sentences: What type of document is this? What is the central question or problem being addressed?",
    "main_goal": "State the primary objective/hypothesis in plain language. What are the authors trying to show or build?",
    "key_findings": [
        "Finding 1: The most important result or claim, with supporting evidence",
        "Finding 2: Second most important result",
        "Finding 3: Third most important result"
    ],
    "methodology": "How was the research conducted? What techniques, models, datasets, or frameworks were used? Be specific about architecture details, training procedures, evaluation metrics.",
    "distinctive_features": "What makes this work unique compared to existing literature? What is the novel contribution?",
    "limitations": "What did the authors acknowledge as weaknesses? What remains unanswered? What assumptions seem questionable?",
    "implications": "Why does this matter? What are the practical or theoretical consequences? How might this change the field?",
    "critical_assessment": "Are the conclusions well-supported by the evidence? Are there any assumptions that seem questionable? How does this fit into the broader field? Comment on sample sizes, statistical significance, or logical structure as appropriate.",
    "author_info": "2-4 sentences about the authors based on your web search. Include current affiliations, notable prior work (with specific paper names), h-index or citation counts if found, and research focus areas.",
    "reliability_assessment": "Rate as HIGH/MEDIUM/LOW confidence. Consider: author track record and citations, institutional affiliation, peer-review status vs preprint, methodology rigor, whether claims are proportionate to evidence, any red flags or concerns.",
    "key_terms": [
        {{"term": "Technical Term", "definition": "Clear, concise definition essential to understanding the work"}},
        {{"term": "Another Term", "definition": "Definition"}}
    ],
    "related_papers": [
        {{
            "title": "Exact title of a real, existing paper",
            "url": "URL (verify via search)",
            "year": 2024,
            "summary": "2-3 sentences summarizing this paper.",
            "priority": "Essential | Recommended | Optional",
            "relevance": "Why this is relevant: e.g., foundational work this paper builds on, contrasting approach, deeper dive into a method, follow-up work"
        }}
    ]
}}

## Guidelines for related papers:
- Suggest 2-4 related papers. They MUST be real — verify via web search.
- Prioritize: (1) foundational papers this builds on, (2) contrasting/competing approaches, (3) methodological references, (4) recent follow-up work.
- Label priority as "Essential" (must-read), "Recommended" (valuable context), or "Optional" (deeper exploration).

Return ONLY the JSON, no other text."""


def _extract_text_from_response(response) -> str:
    """Extract text content from a response that may contain thinking/tool blocks.

    With web search + extended thinking, responses can have many block types.
    We want the last text block, which contains the final JSON answer.
    If stop_reason is 'end_turn' but no text block exists, the model may have
    ended in a tool_use block — we need to handle that.
    """
    text_blocks = [b.text for b in response.content if b.type == "text"]
    if text_blocks:
        # Return the last text block (final answer after tool use)
        return text_blocks[-1]
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

    for attempt in range(3):
        try:
            response = client.messages.create(
                model=model,
                max_tokens=32000,
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
            break
        except anthropic.APIStatusError as e:
            if e.status_code in (429, 529) and attempt < 2:
                wait = 2 ** attempt * 15
                log.warning("API overloaded/rate-limited for '%s', retrying in %ds...", paper.title, wait)
                time.sleep(wait)
            else:
                raise

    raw_text = _extract_text_from_response(response)
    if not raw_text:
        block_types = [b.type for b in response.content]
        stop = getattr(response, "stop_reason", "unknown")
        log.warning(
            "No text content in response for '%s' (stop_reason=%s, blocks=%s)",
            paper.title, stop, block_types,
        )
        raise ValueError(f"No text in response for '{paper.title}' (stop={stop})")

    data = json.loads(extract_json(raw_text))

    related = [
        RelatedPaper(
            title=r["title"],
            url=r.get("url", ""),
            year=r.get("year", 0),
            summary=r.get("summary", ""),
            priority=r.get("priority", ""),
            relevance=r.get("relevance", ""),
        )
        for r in data.get("related_papers", [])
    ]

    key_terms = [
        KeyTerm(term=t["term"], definition=t["definition"])
        for t in data.get("key_terms", [])
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
        document_type=data.get("document_type", ""),
        plain_language_summary=data.get("plain_language_summary", ""),
        overview=data.get("overview", ""),
        main_goal=data.get("main_goal", ""),
        key_findings=data.get("key_findings", []),
        methodology=data.get("methodology", ""),
        distinctive_features=data.get("distinctive_features", ""),
        limitations=data.get("limitations", ""),
        implications=data.get("implications", ""),
        critical_assessment=data.get("critical_assessment", ""),
        author_info=data.get("author_info", ""),
        reliability_assessment=data.get("reliability_assessment", ""),
        key_terms=key_terms,
        related_papers=related,
    )
