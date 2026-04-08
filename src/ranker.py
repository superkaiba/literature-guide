from __future__ import annotations

import json
import logging
import time

import anthropic

from src.json_utils import extract_json

log = logging.getLogger(__name__)

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
        for attempt in range(3):
            try:
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
                break
            except anthropic.APIStatusError as e:
                if e.status_code in (429, 529) and attempt < 2:
                    log.warning("API overloaded/rate-limited, retrying in %ds...", 2 ** attempt * 5)
                    time.sleep(2 ** attempt * 5)
                else:
                    raise
        try:
            raw_text = response.content[0].text
            scores = json.loads(extract_json(raw_text))
        except (json.JSONDecodeError, IndexError) as e:
            log.warning("Failed to parse ranker response: %s", e)
            continue
        for item in scores:
            idx = item.get("index", -1)
            if 0 <= idx < len(batch):
                all_scored.append((batch[idx], item["score"], item.get("topics", [])))

    all_scored.sort(key=lambda x: x[1], reverse=True)
    return all_scored[:max_papers]
