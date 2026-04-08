from __future__ import annotations
from datetime import datetime, timedelta, timezone
import feedparser
from src.models import RawPaper


def _parse_date(entry: dict) -> str:
    parsed = entry.get("published_parsed")
    if parsed:
        try:
            dt = datetime(*parsed[:6], tzinfo=timezone.utc)
            return dt.date().isoformat()
        except (TypeError, ValueError):
            pass
    return datetime.now(timezone.utc).date().isoformat()


def _is_recent(entry: dict, days_back: int) -> bool:
    parsed = entry.get("published_parsed")
    if not parsed:
        return True
    try:
        dt = datetime(*parsed[:6], tzinfo=timezone.utc)
        cutoff = datetime.now(timezone.utc) - timedelta(days=days_back)
        return dt >= cutoff
    except (TypeError, ValueError):
        return True


def fetch_rss(feeds: dict[str, str], days_back: int = 1) -> list[RawPaper]:
    papers: list[RawPaper] = []
    seen_urls: set[str] = set()
    for source_name, feed_url in feeds.items():
        feed = feedparser.parse(feed_url)
        for entry in feed.get("entries", []):
            if not _is_recent(entry, days_back):
                continue
            url = entry.get("link", "")
            if url in seen_urls:
                continue
            seen_urls.add(url)
            authors = [a.get("name", "") for a in entry.get("authors", [])]
            tags = [t.get("term", "") for t in entry.get("tags", [])]
            papers.append(
                RawPaper(
                    title=entry.get("title", "").strip(),
                    authors=[a for a in authors if a],
                    abstract=entry.get("summary", "").strip(),
                    url=url,
                    source=source_name,
                    published_date=_parse_date(entry),
                    doi=None,
                    tags=tags,
                )
            )
    return papers
