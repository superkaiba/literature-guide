from unittest.mock import patch, MagicMock
from src.notify import send_email_notification
from src.models import SummarizedPaper, Opportunity


def _sample_paper(title="Test Paper"):
    return SummarizedPaper(
        id="2026-04-07_test",
        title=title,
        authors=["A"],
        url="https://example.com",
        doi=None,
        source="arxiv",
        published_date="2026-04-06",
        fetched_date="2026-04-07",
        topics=["safety"],
        relevance_score=0.9,
        summary="Summary here.",
        why_it_matters="Important.",
        related_papers=[],
    )


@patch("src.notify.smtplib.SMTP")
def test_send_email_sends_via_smtp(mock_smtp_cls):
    mock_server = MagicMock()
    mock_smtp_cls.return_value.__enter__ = MagicMock(return_value=mock_server)
    mock_smtp_cls.return_value.__exit__ = MagicMock(return_value=False)

    papers = [_sample_paper("Paper A"), _sample_paper("Paper B")]
    opps = [
        Opportunity(title="Job", url="https://x.com", organization="Org", category="job")
    ]
    send_email_notification(
        papers,
        opps,
        report_url="https://github.com/user/repo/blob/main/reports/2026-04-07.md",
        to_email="test@example.com",
        smtp_user="sender@gmail.com",
        smtp_password="app-password",
    )
    mock_server.starttls.assert_called_once()
    mock_server.login.assert_called_once_with("sender@gmail.com", "app-password")
    mock_server.sendmail.assert_called_once()
    args = mock_server.sendmail.call_args[0]
    assert args[0] == "sender@gmail.com"
    assert args[1] == "test@example.com"
    assert "Paper A" in args[2]


@patch("src.notify.smtplib.SMTP")
def test_send_email_skips_if_no_credentials(mock_smtp_cls):
    send_email_notification(
        [], [], report_url="", to_email="", smtp_user="", smtp_password=""
    )
    mock_smtp_cls.assert_not_called()
