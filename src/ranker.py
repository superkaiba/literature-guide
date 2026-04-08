from __future__ import annotations

import json
import logging
import time

import anthropic

from src.json_utils import extract_json

log = logging.getLogger(__name__)

from src.models import RawPaper

RANK_PROMPT = """You are a research paper relevance scorer for an ML researcher.

## About the researcher
They are focused on mechanistic interpretability, AI safety, alignment, language model personas, and weird generalization phenomena (emergent misalignment, subliminal learning, superposition). They want to stay current with the broader ML/AI field as well.

## Their specific research interests:
{topics}

## Scoring instructions

Score each paper's relevance from 0.0 to 1.0 using BOTH criteria:

**Criterion 1 — Topic relevance:**
- 0.9-1.0: Directly about one of the researcher's specific interests
- 0.7-0.9: Closely related to their interests
- 0.4-0.7: Tangentially related

**Criterion 2 — General importance (applies even if not topic-relevant):**
- Any paper that represents a major advance in ML/AI (new SOTA, breakthrough architecture, important benchmark result, significant finding from a top lab) should score AT LEAST 0.6, even if it's outside the researcher's specific topics
- Landmark papers from Anthropic, DeepMind, OpenAI, Meta AI, Google Brain, etc. on foundation models, capabilities, or safety should score at least 0.7

Use the HIGHER of the two scores.

## Papers to score:
{papers}

Return a JSON array with one object per paper:
[{{"index": 0, "score": 0.95, "topics": ["topic1", "topic2"]}}, ...]

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
                    wait = 2 ** attempt * 15
                    log.warning("API overloaded/rate-limited, retrying in %ds...", wait)
                    time.sleep(wait)
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
