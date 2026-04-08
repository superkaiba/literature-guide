from unittest.mock import patch, MagicMock
from src.fetchers.arxiv_fetcher import fetch_arxiv
from src.models import RawPaper

def _mock_result(title="Test Paper", entry_id="http://arxiv.org/abs/2026.12345", doi="10.1234/test"):
    from datetime import datetime, timezone
    r = MagicMock()
    r.title = title
    author1 = MagicMock(); author1.name = "Author A"
    r.authors = [author1]
    r.summary = "Abstract text"
    r.entry_id = entry_id
    r.doi = doi
    r.published = datetime.now(timezone.utc)
    r.categories = []
    return r

@patch("src.fetchers.arxiv_fetcher.arxiv.Client")
def test_fetch_arxiv_returns_raw_papers(mock_client_cls):
    mock_client = MagicMock()
    mock_client.results.return_value = [_mock_result()]
    mock_client_cls.return_value = mock_client
    papers = fetch_arxiv(["mechanistic interpretability"])
    assert len(papers) >= 1
    assert isinstance(papers[0], RawPaper)
    assert papers[0].source == "arxiv"

@patch("src.fetchers.arxiv_fetcher.arxiv.Client")
def test_fetch_arxiv_deduplicates_across_queries(mock_client_cls):
    result = _mock_result()
    mock_client = MagicMock()
    mock_client.results.return_value = [result]
    mock_client_cls.return_value = mock_client
    papers = fetch_arxiv(["query1", "query2"])
    assert len(papers) == 1
