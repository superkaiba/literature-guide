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
                        topics=", ".join(topics), papers=batch_text
                    ),
                }
            ],
        )
        scores = json.loads(response.content[0].text)
        for item in scores:
            idx = item["index"]
            if idx < len(batch):
                all_scored.append((batch[idx], item["score"], item.get("topics", [])))

    all_scored.sort(key=lambda x: x[1], reverse=True)
    return all_scored[:max_papers]
