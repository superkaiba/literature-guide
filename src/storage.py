from __future__ import annotations

import json
import os

from src.models import SummarizedPaper


def _paper_to_markdown(paper: SummarizedPaper) -> str:
    lines = [
        "---",
        f'title: "{paper.title}"',
        f"authors: {paper.authors}",
        f"url: {paper.url}",
        f"source: {paper.source}",
        f"published_date: {paper.published_date}",
        f"topics: {paper.topics}",
        f"relevance_score: {paper.relevance_score}",
        "---",
        "",
        "## Summary",
        paper.summary,
        "",
        "## About the Authors",
        paper.author_info or "No author information available.",
        "",
        "## Reliability Assessment",
        paper.reliability_assessment or "No assessment available.",
        "",
        "## Why It Matters",
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

    filename = f"{paper.id}.md"
    filepath = os.path.join(papers_dir, filename)
    with open(filepath, "w") as f:
        f.write(_paper_to_markdown(paper))

    paper.summary_file = f"papers/{filename}"

    index_path = os.path.join(base_dir, "papers.json")
    index = load_index(base_dir)
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
