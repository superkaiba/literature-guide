from __future__ import annotations

from rapidfuzz import fuzz

from src.models import RawPaper

TITLE_SIMILARITY_THRESHOLD = 85
SOURCE_PRIORITY = {"arxiv": 0, "semantic_scholar": 1, "openalex": 2}


def _normalize_title(title: str) -> str:
    return " ".join(title.lower().split())


def deduplicate(papers: list[RawPaper]) -> list[RawPaper]:
    papers_sorted = sorted(papers, key=lambda p: SOURCE_PRIORITY.get(p.source, 99))

    doi_groups: dict[str, RawPaper] = {}
    no_doi: list[RawPaper] = []
    for p in papers_sorted:
        if p.doi:
            normalized_doi = p.doi.lower().strip()
            if normalized_doi not in doi_groups:
                doi_groups[normalized_doi] = p
        else:
            no_doi.append(p)

    candidates = list(doi_groups.values()) + no_doi

    result: list[RawPaper] = []
    for paper in candidates:
        norm = _normalize_title(paper.title)
        is_dup = False
        for existing in result:
            if fuzz.ratio(norm, _normalize_title(existing.title)) >= TITLE_SIMILARITY_THRESHOLD:
                is_dup = True
                break
        if not is_dup:
            result.append(paper)

    return result
