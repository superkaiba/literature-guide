from datetime import datetime, timezone
import responses
from src.fetchers.bluesky import fetch_bluesky

# Use a recent ISO timestamp
_now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

SAMPLE_RESPONSE = {
    "feed": [{"post": {
        "uri": "at://did:plc:abc/app.bsky.feed.post/123",
        "author": {"handle": "researcher.bsky.social", "displayName": "Dr. Researcher"},
        "record": {"text": "New paper: deception in fine-tuned models https://arxiv.org/abs/2026.11111", "createdAt": _now_iso},
        "embed": {"$type": "app.bsky.embed.external#view", "external": {
            "uri": "https://arxiv.org/abs/2026.11111",
            "title": "Emergent Deception in Fine-tuned Models",
            "description": "We study emergent deception.",
        }},
    }}]
}

@responses.activate
def test_fetch_bluesky_extracts_links():
    responses.add(responses.GET, "https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed", json=SAMPLE_RESPONSE, status=200)
    papers = fetch_bluesky(["researcher.bsky.social"])
    assert len(papers) >= 1
    assert papers[0].source == "bluesky"
