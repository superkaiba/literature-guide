from __future__ import annotations
from datetime import date, timedelta
import requests
from src.models import RawPaper


def _reconstruct_abstract(inverted_index: dict | None) -> str:
    if not inverted_index:
        return ""
    word_positions: list[tuple[int, str]] = []
    for word, positions in inverted_index.items():
        for pos in positions:
            word_positions.append((pos, word))
    word_positions.sort()
    return " ".join(w for _, w in word_positions)


def fetch_openalex(queries: list[str], days_back: int = 1) -> list[RawPaper]:
    cutoff = (date.today() - timedelta(days=days_back)).isoformat()
    seen_ids: set[str] = set()
    papers: list[RawPaper] = []
    for query in queries:
        resp = requests.get(
            "https://api.openalex.org/works",
            params={
                "search": query,
                "filter": f"from_publication_date:{cutoff}",
                "sort": "publication_date:desc",
                "per_page": 25,
            },
            headers={"User-Agent": "literature-guide/1.0"},
            timeout=30,
        )
        resp.raise_for_status()
        for work in resp.json().get("results", []):
            oa_id = work.get("id", "")
            if oa_id in seen_ids:
                continue
            seen_ids.add(oa_id)
            papers.append(
                RawPaper(
                    title=work.get("title", "").strip(),
                    authors=[
                        a["author"]["display_name"]
                        for a in work.get("authorships", [])
                    ],
                    abstract=_reconstruct_abstract(
                        work.get("abstract_inverted_index")
                    ),
                    url=work.get("doi") or oa_id,
                    source="openalex",
                    published_date=work.get("publication_date", ""),
                    doi=work.get("doi"),
                    tags=[t["display_name"] for t in work.get("topics", [])],
                )
            )
    return papers
