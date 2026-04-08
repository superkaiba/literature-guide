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
        f"document_type: {paper.document_type}",
        f"topics: {paper.topics}",
        f"relevance_score: {paper.relevance_score}",
        "---",
        "",
        f"# {paper.title}",
        "",
    ]

    if paper.overview:
        lines.extend(["## Overview", paper.overview, ""])

    if paper.author_info:
        lines.extend(["## About the Authors", paper.author_info, ""])

    if paper.reliability_assessment:
        lines.extend(["## Reliability Assessment", paper.reliability_assessment, ""])

    if paper.main_goal:
        lines.extend(["## Main Goal", paper.main_goal, ""])

    if paper.key_findings:
        lines.append("## Key Findings")
        for f_ in paper.key_findings:
            lines.append(f"- {f_}")
        lines.append("")

    if paper.methodology:
        lines.extend(["## Methodology", paper.methodology, ""])

    if paper.distinctive_features:
        lines.extend(["## What's Novel", paper.distinctive_features, ""])

    if paper.limitations:
        lines.extend(["## Limitations & Open Questions", paper.limitations, ""])

    if paper.implications:
        lines.extend(["## Implications", paper.implications, ""])

    if paper.critical_assessment:
        lines.extend(["## Critical Assessment", paper.critical_assessment, ""])

    if paper.key_terms:
        lines.append("## Key Terms")
        for kt in paper.key_terms:
            lines.append(f"- **{kt.term}:** {kt.definition}")
        lines.append("")

    if paper.related_papers:
        lines.append("## Related Papers")
        for rp in paper.related_papers:
            url_part = f"({rp.url})" if rp.url else ""
            priority = f" — *{rp.priority}*" if rp.priority else ""
            lines.append(f"### [{rp.title}]{url_part} ({rp.year}){priority}")
            lines.append(rp.summary)
            if rp.relevance:
                lines.append(f"*Why relevant: {rp.relevance}*")
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
