from __future__ import annotations
from datetime import datetime, timedelta, timezone
import arxiv
from src.models import RawPaper


def fetch_arxiv(queries: list[str], days_back: int = 1) -> list[RawPaper]:
    cutoff_date = datetime.now(timezone.utc).date() - timedelta(days=days_back)
    cutoff = datetime(cutoff_date.year, cutoff_date.month, cutoff_date.day, tzinfo=timezone.utc)
    seen_ids: set[str] = set()
    papers: list[RawPaper] = []
    client = arxiv.Client()
    for query in queries:
        search = arxiv.Search(
            query=query,
            max_results=50,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )
        for result in client.results(search):
            pub_date = result.published.replace(tzinfo=timezone.utc)
            if pub_date < cutoff:
                continue
            if result.entry_id in seen_ids:
                continue
            seen_ids.add(result.entry_id)
            papers.append(
                RawPaper(
                    title=result.title.strip(),
                    authors=[a.name for a in result.authors],
                    abstract=result.summary.strip(),
                    url=result.entry_id,
                    source="arxiv",
                    published_date=pub_date.date().isoformat(),
                    doi=result.doi,
                    tags=[
                        c.term if hasattr(c, "term") else str(c)
                        for c in (result.categories or [])
                    ],
                )
            )
    return papers
