from unittest.mock import patch, MagicMock
from src.ranker import rank_papers
from src.models import RawPaper


def _paper(title, abstract=""):
    return RawPaper(
        title=title,
        authors=["A"],
        abstract=abstract,
        url="https://example.com",
        source="arxiv",
        published_date="2026-04-06",
        tags=[],
    )


@patch("src.ranker.anthropic.Anthropic")
def test_rank_papers_returns_scored_list(mock_anthropic_cls):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.content = [MagicMock()]
    mock_response.content[0].text = '[{"index": 0, "score": 0.95, "topics": ["mechanistic interpretability"]}, {"index": 1, "score": 0.3, "topics": ["computer vision"]}]'
    mock_client.messages.create.return_value = mock_response
    mock_anthropic_cls.return_value = mock_client

    papers = [
        _paper("SAE Features in GPT-4", "We study sparse autoencoder features."),
        _paper("Image Classification Survey", "A survey of CNN architectures."),
    ]
    scored = rank_papers(papers, ["mechanistic interpretability", "AI safety"], api_key="test")
    assert len(scored) == 2
    assert scored[0][1] >= scored[1][1]


@patch("src.ranker.anthropic.Anthropic")
def test_rank_papers_filters_by_max(mock_anthropic_cls):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.content = [MagicMock()]
    mock_response.content[0].text = '[{"index": 0, "score": 0.9, "topics": ["safety"]}, {"index": 1, "score": 0.8, "topics": ["alignment"]}, {"index": 2, "score": 0.1, "topics": []}]'
    mock_client.messages.create.return_value = mock_response
    mock_anthropic_cls.return_value = mock_client

    papers = [_paper(f"Paper {i}") for i in range(3)]
    scored = rank_papers(papers, ["safety"], api_key="test", max_papers=2)
    assert len(scored) == 2
