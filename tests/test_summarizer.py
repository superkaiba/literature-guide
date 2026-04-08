from unittest.mock import patch, MagicMock
from src.summarizer import summarize_paper
from src.models import RawPaper, SummarizedPaper


@patch("src.summarizer.anthropic.Anthropic")
def test_summarize_paper_returns_summarized(mock_anthropic_cls):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.content = [MagicMock()]
    mock_response.content[0].text = '{"summary": "This paper studies sparse autoencoders for extracting interpretable features.", "why_it_matters": "Directly advances mechanistic interpretability.", "related_papers": [{"title": "Toy Models of Superposition", "url": "https://arxiv.org/abs/2209.10652", "year": 2022, "summary": "Foundational work on superposition."}]}'
    mock_client.messages.create.return_value = mock_response
    mock_anthropic_cls.return_value = mock_client

    paper = RawPaper(
        title="Scaling SAEs",
        authors=["A", "B"],
        abstract="We scale sparse autoencoders to GPT-4.",
        url="https://arxiv.org/abs/2026.12345",
        source="arxiv",
        published_date="2026-04-06",
        tags=[],
    )
    result = summarize_paper(
        paper, ["mechanistic interpretability"], score=0.95, api_key="test"
    )
    assert isinstance(result, SummarizedPaper)
    assert "sparse autoencoders" in result.summary
    assert len(result.related_papers) == 1
    assert result.related_papers[0].year == 2022
    assert result.relevance_score == 0.95
