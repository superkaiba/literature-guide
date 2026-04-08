import json
import os
import shutil
from unittest.mock import patch, MagicMock
from datetime import datetime, timezone
from src.main import run_pipeline


@patch("src.main.send_email_notification")
@patch("src.fetchers.bluesky.requests.get")
@patch("src.fetchers.reddit.requests.get")
@patch("src.fetchers.rss.feedparser.parse")
@patch("src.fetchers.semantic_scholar.requests.get")
@patch("src.fetchers.openalex.requests.get")
@patch("src.fetchers.arxiv_fetcher.arxiv.Client")
def test_full_pipeline_dry_run(mock_arxiv_client, mock_openalex, mock_s2, mock_rss, mock_reddit, mock_bsky, mock_notify, tmp_path, monkeypatch):
    # Capture original working directory before chdir
    original_dir = os.getcwd()
    monkeypatch.chdir(tmp_path)
    shutil.copy(os.path.join(original_dir, "config.yml"), str(tmp_path / "config.yml"))
    (tmp_path / "papers.json").write_text("[]")
    os.makedirs(tmp_path / "papers", exist_ok=True)
    os.makedirs(tmp_path / "reports", exist_ok=True)

    # Mock arXiv - one paper
    mock_result = MagicMock()
    mock_result.title = "Interpretability via SAEs"
    author = MagicMock(); author.name = "Test Author"
    mock_result.authors = [author]
    mock_result.summary = "We study sparse autoencoders."
    mock_result.entry_id = "http://arxiv.org/abs/2026.12345"
    mock_result.doi = None
    mock_result.published = datetime.now(timezone.utc)
    mock_result.categories = []
    client = MagicMock()
    client.results.return_value = [mock_result]
    mock_arxiv_client.return_value = client

    # Other fetchers return empty
    mock_openalex.return_value = MagicMock(status_code=200, json=lambda: {"results": []})
    mock_s2.return_value = MagicMock(status_code=200, json=lambda: {"data": []})
    mock_rss.return_value = {"entries": [], "bozo": False}
    mock_reddit.return_value = MagicMock(status_code=200, json=lambda: {"data": {"children": []}})
    mock_bsky.return_value = MagicMock(status_code=200, json=lambda: {"feed": []})

    # Mock Anthropic API — single mock since both ranker and summarizer share the same
    # anthropic module. Use side_effect to return different clients for each instantiation.
    ranker_client = MagicMock()
    ranker_response = MagicMock()
    ranker_response.content = [MagicMock()]
    ranker_response.content[0].text = '[{"index": 0, "score": 0.95, "topics": ["mechanistic interpretability"]}]'
    ranker_client.messages.create.return_value = ranker_response

    summarizer_client = MagicMock()
    summarizer_response = MagicMock()
    summarizer_response.content = [MagicMock()]
    summarizer_response.content[0].text = json.dumps({
        "summary": "This paper studies SAEs for interpretability.",
        "why_it_matters": "Advances mechanistic interpretability.",
        "author_info": "Test Author is a researcher at Anthropic.",
        "reliability_assessment": "HIGH confidence. Published by established researchers.",
        "related_papers": [{"title": "Toy Models of Superposition", "url": "https://arxiv.org/abs/2209.10652", "year": 2022, "summary": "Foundational work on superposition."}]
    })
    summarizer_client.messages.create.return_value = summarizer_response

    # The ranker is called first, then the summarizer
    anthropic_clients = [ranker_client, summarizer_client]
    call_index = {"i": 0}

    def make_client(**kwargs):
        idx = call_index["i"]
        call_index["i"] += 1
        return anthropic_clients[idx] if idx < len(anthropic_clients) else MagicMock()

    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    monkeypatch.setenv("EMAIL_TO", "test@example.com")
    monkeypatch.setenv("SMTP_USER", "sender@gmail.com")
    monkeypatch.setenv("SMTP_PASSWORD", "app-password")

    with patch("anthropic.Anthropic", side_effect=make_client):
        run_pipeline(config_path=str(tmp_path / "config.yml"))

    reports = list((tmp_path / "reports").iterdir())
    assert len(reports) == 1
    papers_dir = list((tmp_path / "papers").iterdir())
    assert len(papers_dir) >= 1
    index = json.loads((tmp_path / "papers.json").read_text())
    assert len(index) == 1
    mock_notify.assert_called_once()
