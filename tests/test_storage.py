import json
from src.storage import save_paper, load_index
from src.models import SummarizedPaper, RelatedPaper, KeyTerm


def _sample_paper():
    return SummarizedPaper(
        id="2026-04-07_test-paper", title="Test Paper",
        authors=["Alice", "Bob"], url="https://arxiv.org/abs/2026.12345",
        doi="10.1234/test", source="arxiv",
        published_date="2026-04-06", fetched_date="2026-04-07",
        topics=["mechanistic interpretability"], relevance_score=0.95,
        document_type="research paper",
        overview="A paper about mechanistic interpretability.",
        main_goal="Understand model internals.",
        key_findings=["Features are interpretable", "SAEs work well"],
        methodology="Trained SAEs on GPT-2.",
        distinctive_features="First to scale SAEs.",
        limitations="Only tested on small models.",
        implications="Scalable interpretability.",
        critical_assessment="Strong methodology.",
        author_info="Alice and Bob are at MIT CSAIL.",
        reliability_assessment="HIGH confidence.",
        key_terms=[KeyTerm(term="SAE", definition="Sparse Autoencoder")],
        related_papers=[
            RelatedPaper(title="Related Work", url="https://arxiv.org/abs/2024.11111",
                         year=2024, summary="Earlier work on Y.",
                         priority="Essential", relevance="Foundational")
        ],
    )


def test_save_paper_creates_markdown(tmp_path):
    paper = _sample_paper()
    save_paper(paper, base_dir=str(tmp_path))
    md_path = tmp_path / "papers" / "2026-04-07_test-paper.md"
    assert md_path.exists()
    content = md_path.read_text()
    assert "Test Paper" in content
    assert "Related Work" in content
    assert "Key Findings" in content
    assert "SAE" in content


def test_save_paper_updates_index(tmp_path):
    (tmp_path / "papers.json").write_text("[]")
    save_paper(_sample_paper(), base_dir=str(tmp_path))
    index = load_index(str(tmp_path))
    assert len(index) == 1
    assert index[0]["id"] == "2026-04-07_test-paper"


def test_save_paper_no_duplicate_in_index(tmp_path):
    (tmp_path / "papers.json").write_text("[]")
    paper = _sample_paper()
    save_paper(paper, base_dir=str(tmp_path))
    save_paper(paper, base_dir=str(tmp_path))
    index = load_index(str(tmp_path))
    assert len(index) == 1
