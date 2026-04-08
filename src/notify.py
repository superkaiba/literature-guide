from __future__ import annotations

from datetime import date

import requests

from src.models import SummarizedPaper, Opportunity


def _format_slack_message(
    papers: list[SummarizedPaper],
    opportunities: list[Opportunity],
    report_url: str,
) -> str:
    today = date.today().isoformat()
    lines = [f":newspaper: *Literature Guide — {today}*", ""]

    if papers:
        lines.append("*Top Papers:*")
        for i, p in enumerate(papers[:5], 1):
            first_sentence = p.summary.split(".")[0] + "."
            lines.append(f"{i}. <{p.url}|{p.title}> — {first_sentence}")
        lines.append("")

    if opportunities:
        job_count = sum(
            1 for o in opportunities if o.category in ("job", "fellowship")
        )
        cfp_count = sum(1 for o in opportunities if o.category == "cfp")
        parts = []
        if job_count:
            parts.append(f"{job_count} job{'s' if job_count > 1 else ''}")
        if cfp_count:
            parts.append(f"{cfp_count} CFP{'s' if cfp_count > 1 else ''}")
        other = len(opportunities) - job_count - cfp_count
        if other:
            parts.append(f"{other} other")
        lines.append(
            f"*Opportunities:* {len(opportunities)} new ({', '.join(parts)})"
        )
        lines.append("")

    lines.append(f":link: <{report_url}|Full report>")
    return "\n".join(lines)


def send_slack_notification(
    papers: list[SummarizedPaper],
    opportunities: list[Opportunity],
    webhook_url: str,
    report_url: str,
) -> None:
    if not webhook_url:
        return

    message = _format_slack_message(papers, opportunities, report_url)
    requests.post(webhook_url, json={"text": message}, timeout=30)
