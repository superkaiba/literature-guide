from __future__ import annotations
from datetime import date, timedelta
import requests
from src.models import RawPaper

API_BASE = "https://api.semanticscholar.org/graph/v1"


def fetch_semantic_scholar(
    queries: list[str], api_key: str = "", days_back: int = 1
) -> list[RawPaper]:
    cutoff = (date.today() - timedelta(days=days_back)).isoformat()
    seen_ids: set[str] = set()
    papers: list[RawPaper] = []
    headers = {}
    if api_key:
        headers["x-api-key"] = api_key
    for query in queries:
        resp = requests.get(
            f"{API_BASE}/paper/search",
            params={
                "query": query,
                "limit": 25,
                "fields": "title,authors,abstract,url,externalIds,publicationDate,fieldsOfStudy",
                "publicationDateOrYear": f"{cutoff}:",
            },
            headers=headers,
            timeout=30,
        )
        if resp.status_code == 429:
            continue
        resp.raise_for_status()
        for paper in resp.json().get("data", []):
            pid = paper.get("paperId", "")
            if pid in seen_ids or not paper.get("title"):
                continue
            seen_ids.add(pid)
            ext_ids = paper.get("externalIds") or {}
            papers.append(
                RawPaper(
                    title=paper["title"].strip(),
                    authors=[a["name"] for a in paper.get("authors", [])],
                    abstract=(paper.get("abstract") or "").strip(),
                    url=paper.get("url")
                    or f"https://www.semanticscholar.org/paper/{pid}",
                    source="semantic_scholar",
                    published_date=paper.get("publicationDate") or "",
                    doi=ext_ids.get("DOI"),
                    tags=paper.get("fieldsOfStudy") or [],
                )
            )
    return papers
