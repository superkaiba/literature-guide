import time
import responses
from src.fetchers.reddit import fetch_reddit

# Use a recent UTC timestamp so the post passes recency checks
_recent_utc = time.time()

SAMPLE_RESPONSE = {
    "data": {"children": [{"data": {
        "title": "[R] New paper on emergent misalignment",
        "url": "https://arxiv.org/abs/2026.99999",
        "selftext": "Interesting new paper on emergent misalignment in fine-tuned models.",
        "author": "researcher123", "created_utc": _recent_utc,
        "link_flair_text": "Research", "score": 150,
    }}]}
}

@responses.activate
def test_fetch_reddit_returns_papers():
    responses.add(responses.GET, "https://old.reddit.com/r/MachineLearning/new.json", json=SAMPLE_RESPONSE, status=200)
    papers = fetch_reddit(["MachineLearning"])
    assert len(papers) == 1
    assert papers[0].source == "reddit_MachineLearning"
