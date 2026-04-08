from unittest.mock import patch, MagicMock
from src.summarizer import summarize_paper
from src.models import RawPaper, SummarizedPaper


MOCK_RESPONSE_JSON = """{
    "document_type": "research paper",
    "overview": "This is a research paper that studies sparse autoencoders for extracting interpretable features from language models. It addresses the challenge of scaling interpretability methods.",
    "main_goal": "Scale sparse autoencoders to GPT-4 class models and evaluate whether feature decomposition remains consistent.",
    "key_findings": [
        "SAE features are consistently interpretable across model scales",
        "Feature splitting occurs predictably with model size",
        "Reconstruction quality improves with larger dictionaries"
    ],
    "methodology": "Trained sparse autoencoders on activations from GPT-2 through GPT-4 with varying dictionary sizes. Evaluated using automated interpretability scores and human raters.",
    "distinctive_features": "First systematic study of SAE scaling behavior across multiple orders of magnitude in model size.",
    "limitations": "Only evaluated on English text. Human evaluation was limited to 500 features per model.",
    "implications": "Suggests mechanistic interpretability via SAEs is viable at frontier model scale, which could enable safety auditing of production systems.",
    "critical_assessment": "Strong methodology with appropriate controls. The automated interpretability metric correlates well with human judgment (r=0.85). However, the claim about production readiness may be premature given the compute costs.",
    "author_info": "Authors A and B are researchers at Anthropic, known for their work on interpretability. A previously published Toy Models of Superposition (2022).",
    "reliability_assessment": "HIGH confidence. Authors are established researchers at a leading AI safety lab with strong publication records. Methodology is rigorous with appropriate ablations.",
    "key_terms": [
        {"term": "Sparse Autoencoder (SAE)", "definition": "Neural network trained to decompose activations into sparse, interpretable features"},
        {"term": "Feature splitting", "definition": "Phenomenon where a single feature splits into multiple more specific features as dictionary size increases"}
    ],
    "related_papers": [
        {
            "title": "Toy Models of Superposition",
            "url": "https://arxiv.org/abs/2209.10652",
            "year": 2022,
            "summary": "Foundational work showing how neural networks represent more features than dimensions through superposition.",
            "priority": "Essential",
            "relevance": "Theoretical foundation that this paper's SAE approach directly builds upon."
        }
    ]
}"""


@patch("src.summarizer.anthropic.Anthropic")
def test_summarize_paper_returns_summarized(mock_anthropic_cls):
    mock_client = MagicMock()

    thinking_block = MagicMock()
    thinking_block.type = "thinking"

    text_block = MagicMock()
    text_block.type = "text"
    text_block.text = MOCK_RESPONSE_JSON

    mock_response = MagicMock()
    mock_response.content = [thinking_block, text_block]
    mock_client.messages.create.return_value = mock_response
    mock_anthropic_cls.return_value = mock_client

    paper = RawPaper(
        title="Scaling SAEs", authors=["A", "B"],
        abstract="We scale sparse autoencoders to GPT-4.",
        url="https://arxiv.org/abs/2026.12345",
        source="arxiv", published_date="2026-04-06", tags=[],
    )
    result = summarize_paper(
        paper, ["mechanistic interpretability"], score=0.95, api_key="test"
    )
    assert isinstance(result, SummarizedPaper)
    assert result.document_type == "research paper"
    assert "sparse autoencoders" in result.overview
    assert len(result.key_findings) == 3
    assert result.methodology
    assert result.distinctive_features
    assert result.limitations
    assert result.critical_assessment
    assert len(result.key_terms) == 2
    assert result.key_terms[0].term == "Sparse Autoencoder (SAE)"
    assert len(result.related_papers) == 1
    assert result.related_papers[0].priority == "Essential"
    assert result.related_papers[0].relevance
    assert "Anthropic" in result.author_info
    assert "HIGH" in result.reliability_assessment
    assert result.relevance_score == 0.95

    # Verify Opus + extended thinking + web search
    call_kwargs = mock_client.messages.create.call_args[1]
    assert call_kwargs["model"] == "claude-opus-4-6"
    assert call_kwargs["thinking"]["type"] == "enabled"
    assert any(t.get("name") == "web_search" for t in call_kwargs["tools"])
