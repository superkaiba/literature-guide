from unittest.mock import patch, MagicMock
from src.summarizer import summarize_paper
from src.models import RawPaper, SummarizedPaper


@patch("src.summarizer.anthropic.Anthropic")
def test_summarize_paper_returns_summarized(mock_anthropic_cls):
    mock_client = MagicMock()

    # Simulate response with thinking block + text block
    thinking_block = MagicMock()
    thinking_block.type = "thinking"
    thinking_block.thinking = "Let me analyze this paper..."

    text_block = MagicMock()
    text_block.type = "text"
    text_block.text = '{"summary": "This paper studies sparse autoencoders for extracting interpretable features from language models. The authors scale SAEs to GPT-4 class models and find consistent feature decomposition.", "why_it_matters": "Directly advances mechanistic interpretability by providing scalable feature extraction methods.", "author_info": "Authors A and B are researchers at Anthropic, known for their work on interpretability. A previously published Toy Models of Superposition.", "reliability_assessment": "HIGH confidence. Authors are established researchers at a leading AI safety lab with strong publication records.", "related_papers": [{"title": "Toy Models of Superposition", "url": "https://arxiv.org/abs/2209.10652", "year": 2022, "summary": "Foundational work on superposition in neural networks."}]}'

    mock_response = MagicMock()
    mock_response.content = [thinking_block, text_block]
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
    assert "Anthropic" in result.author_info
    assert "HIGH" in result.reliability_assessment

    # Verify web search tool and extended thinking were passed
    call_kwargs = mock_client.messages.create.call_args[1]
    assert call_kwargs["model"] == "claude-opus-4-6"
    assert call_kwargs["thinking"]["type"] == "enabled"
    assert any(t.get("name") == "web_search" for t in call_kwargs["tools"])
