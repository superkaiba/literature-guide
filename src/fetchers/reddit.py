from __future__ import annotations
from datetime import datetime, timedelta, timezone
import requests
from src.models import RawPaper


def fetch_reddit(subreddits: list[str], days_back: int = 1) -> list[RawPaper]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=days_back)
    papers: list[RawPaper] = []
    for sub in subreddits:
        resp = requests.get(
            f"https://old.reddit.com/r/{sub}/new.json",
            params={"limit": 50},
            headers={"User-Agent": "literature-guide/1.0"},
            timeout=30,
        )
        if resp.status_code != 200:
            continue
        for child in resp.json().get("data", {}).get("children", []):
            post = child["data"]
            created = datetime.fromtimestamp(post["created_utc"], tz=timezone.utc)
            if created < cutoff:
                continue
            papers.append(
                RawPaper(
                    title=post.get("title", "").strip(),
                    authors=[post.get("author", "")],
                    abstract=post.get("selftext", "").strip()[:1000],
                    url=post.get("url", ""),
                    source=f"reddit_{sub}",
                    published_date=created.date().isoformat(),
                    doi=None,
                    tags=[post.get("link_flair_text", "")],
                )
            )
    return papers
