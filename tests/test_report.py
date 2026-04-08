import os
from src.report import generate_report
from src.models import SummarizedPaper, RelatedPaper, Opportunity, KeyTerm


def _sample_paper(title="Test Paper", score=0.9):
    return SummarizedPaper(
        id=f"2026-04-07_{title.lower().replace(' ', '-')}",
        title=title, authors=["Alice"], url="https://example.com",
        doi=None, source="arxiv", published_date="2026-04-06",
        fetched_date="2026-04-07", topics=["safety"], relevance_score=score,
        document_type="research paper",
        plain_language_summary="This paper tests whether AI systems can be tricked into doing bad things.",
        overview="A paper studying safety properties in language models.",
        main_goal="Evaluate safety of LLMs.",
        key_findings=["Models can be jailbroken", "Defenses help"],
        methodology="Red-teaming on GPT-4.",
        distinctive_features="First large-scale red-team study.",
        limitations="Only tested English.",
        implications="Better safety evaluations needed.",
        critical_assessment="Well-designed study with clear results.",
        author_info="Alice is a researcher at Anthropic.",
        reliability_assessment="HIGH confidence. Published by leading lab.",
        key_terms=[KeyTerm(term="Red-teaming", definition="Adversarial testing")],
        related_papers=[
            RelatedPaper(title="Old Paper", url="https://example.com/old",
                         year=2023, summary="Earlier work.",
                         priority="Essential", relevance="Foundational work")
        ],
    )


def test_generate_report_creates_file(tmp_path):
    papers = [_sample_paper("Paper A", 0.95), _sample_paper("Paper B", 0.8)]
    opps = [Opportunity(title="Safety Role", url="https://example.com/job",
                        organization="Anthropic", category="job")]
    path = generate_report(papers, opps, date_str="2026-04-07", base_dir=str(tmp_path))
    assert os.path.exists(path)
    content = open(path).read()
    assert "Literature Guide" in content
    assert "Paper A" in content
    assert "Safety Role" in content
    assert "Highlights" in content
    assert "Key findings" in content
    assert "Methodology" in content


def test_generate_report_has_meta_section(tmp_path):
    papers = [_sample_paper()]
    path = generate_report(papers, [], date_str="2026-04-07",
                           base_dir=str(tmp_path), sources_checked=15, papers_scanned=200)
    content = open(path).read()
    assert "Sources checked: 15" in content
