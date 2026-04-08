from unittest.mock import patch, MagicMock
from src.main import run_pipeline
from src.models import RawPaper, SummarizedPaper, KeyTerm


def _raw_paper():
    return RawPaper(title="Test", authors=["A"], abstract="Abstract", url="https://example.com", source="arxiv", published_date="2026-04-06", tags=[])


def _summarized_paper():
    return SummarizedPaper(
        id="2026-04-07_test", title="Test", authors=["A"],
        url="https://example.com", doi=None, source="arxiv",
        published_date="2026-04-06", fetched_date="2026-04-07",
        topics=["safety"], relevance_score=0.9,
        document_type="research paper",
        plain_language_summary="Plain summary.",
        overview="Overview.",
        main_goal="Goal.", key_findings=["Finding 1"],
        methodology="Method.", distinctive_features="Novel.",
        limitations="Limits.", implications="Implications.",
        critical_assessment="Assessment.",
        author_info="A is at MIT.", reliability_assessment="HIGH.",
        key_terms=[], related_papers=[],
    )


@patch("src.main.send_email_notification")
@patch("src.main.generate_report")
@patch("src.main.save_paper")
@patch("src.main.summarize_paper")
@patch("src.main.rank_papers")
@patch("src.main.deduplicate")
@patch("src.main.fetch_all")
@patch("src.main.load_config")
def test_run_pipeline_orchestrates_all_steps(mock_config, mock_fetch, mock_dedup, mock_rank, mock_summarize, mock_save, mock_report, mock_notify):
    cfg = MagicMock()
    cfg.topics = ["safety"]
    cfg.anthropic_api_key = "test"
    cfg.email_to = "test@example.com"
    cfg.smtp_user = "sender@gmail.com"
    cfg.smtp_password = "app-password"
    cfg.github_repo_url = "https://github.com/user/repo"
    cfg.max_papers = 20
    cfg.max_opportunities = 10
    mock_config.return_value = cfg
    raw = [_raw_paper()]
    mock_fetch.return_value = (raw, [])
    mock_dedup.return_value = raw
    mock_rank.return_value = [(raw[0], 0.9, ["safety"])]
    sp = _summarized_paper()
    mock_summarize.return_value = sp
    mock_report.return_value = "reports/2026-04-07.md"
    run_pipeline()
    mock_fetch.assert_called_once()
    mock_dedup.assert_called_once()
    mock_rank.assert_called_once()
    mock_summarize.assert_called_once()
    mock_save.assert_called_once()
    mock_report.assert_called_once()
    mock_notify.assert_called_once()
