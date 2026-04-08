from __future__ import annotations
import re
from datetime import datetime, timedelta, timezone
import requests
from src.models import RawPaper

BSKY_API = "https://public.api.bsky.app/xrpc"


def _extract_urls(text: str) -> list[str]:
    return re.findall(r"https?://[^\s)]+", text)


def fetch_bluesky(accounts: list[str], days_back: int = 1) -> list[RawPaper]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=days_back)
    papers: list[RawPaper] = []
    seen_urls: set[str] = set()
    for handle in accounts:
        resp = requests.get(
            f"{BSKY_API}/app.bsky.feed.getAuthorFeed",
            params={"actor": handle, "limit": 30},
            timeout=30,
        )
        if resp.status_code != 200:
            continue
        for item in resp.json().get("feed", []):
            post = item.get("post", {})
            record = post.get("record", {})
            created_str = record.get("createdAt", "")
            try:
                created = datetime.fromisoformat(
                    created_str.replace("Z", "+00:00")
                )
            except (ValueError, AttributeError):
                continue
            if created < cutoff:
                continue
            text = record.get("text", "")
            embed = post.get("embed", {})
            external = embed.get("external", {})
            link = external.get("uri", "")
            title = external.get("title", "")
            description = external.get("description", "")
            if not link:
                urls = _extract_urls(text)
                link = urls[0] if urls else ""
            if not link or link in seen_urls:
                continue
            seen_urls.add(link)
            author = post.get("author", {})
            papers.append(
                RawPaper(
                    title=title or text[:120],
                    authors=[author.get("displayName", handle)],
                    abstract=description or text,
                    url=link,
                    source="bluesky",
                    published_date=created.date().isoformat(),
                    doi=None,
                    tags=[],
                )
            )
    return papers
