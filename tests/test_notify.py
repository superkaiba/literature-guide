import json
import responses
from src.notify import send_slack_notification
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


@responses.activate
def test_send_slack_posts_to_webhook():
    responses.add(responses.POST, "https://hooks.slack.com/test", status=200)
    papers = [_sample_paper("Paper A"), _sample_paper("Paper B")]
    opps = [
        Opportunity(
            title="Job",
            url="https://x.com",
            organization="Org",
            category="job",
        )
    ]
    send_slack_notification(
        papers,
        opps,
        webhook_url="https://hooks.slack.com/test",
        report_url="https://github.com/user/repo/blob/main/reports/2026-04-07.md",
    )
    assert len(responses.calls) == 1
    body = json.loads(responses.calls[0].request.body)
    assert "Paper A" in body["text"]
