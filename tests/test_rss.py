from unittest.mock import patch
from src.fetchers.rss import fetch_rss
from datetime import datetime, timezone
import time

# Use a recent timestamp so the entry passes the recency check
_now = datetime.now(timezone.utc)
_recent_parsed = time.gmtime(time.time())

SAMPLE_FEED = {
    "entries": [{
        "title": "New Interpretability Results",
        "link": "https://example.com/post/1",
        "summary": "We found interesting features in transformer MLPs.",
        "authors": [{"name": "Researcher X"}],
        "published_parsed": (_now.year, _now.month, _now.day, 12, 0, 0, 0, 96, 0),
        "tags": [{"term": "interpretability"}],
    }],
    "bozo": False,
}

@patch("src.fetchers.rss.feedparser.parse")
def test_fetch_rss_returns_papers(mock_parse):
    mock_parse.return_value = SAMPLE_FEED
    papers = fetch_rss({"test_blog": "https://example.com/feed.xml"})
    assert len(papers) == 1
    assert papers[0].source == "test_blog"

@patch("src.fetchers.rss.feedparser.parse")
def test_fetch_rss_handles_missing_authors(mock_parse):
    entry = SAMPLE_FEED["entries"][0].copy()
    del entry["authors"]
    mock_parse.return_value = {"entries": [entry], "bozo": False}
    papers = fetch_rss({"blog": "https://example.com/feed"})
    assert papers[0].authors == []
