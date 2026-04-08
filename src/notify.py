from __future__ import annotations

import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.models import SummarizedPaper, Opportunity


def _format_email_html(
    papers: list[SummarizedPaper],
    opportunities: list[Opportunity],
    report_url: str,
) -> str:
    today = date.today().isoformat()
    lines = [
        f"<h2>Literature Guide &mdash; {today}</h2>",
    ]

    if papers:
        lines.append("<h3>Top Papers</h3><ol>")
        for p in papers[:5]:
            first_sentence = p.summary.split(".")[0] + "."
            lines.append(
                f'<li><a href="{p.url}">{p.title}</a> &mdash; {first_sentence}</li>'
            )
        lines.append("</ol>")

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
            f"<p><strong>Opportunities:</strong> {len(opportunities)} new ({', '.join(parts)})</p>"
        )

    lines.append(f'<p><a href="{report_url}">Full report on GitHub</a></p>')
    return "\n".join(lines)


def _format_email_plain(
    papers: list[SummarizedPaper],
    opportunities: list[Opportunity],
    report_url: str,
) -> str:
    today = date.today().isoformat()
    lines = [f"Literature Guide — {today}", ""]

    if papers:
        lines.append("Top Papers:")
        for i, p in enumerate(papers[:5], 1):
            first_sentence = p.summary.split(".")[0] + "."
            lines.append(f"{i}. {p.title} — {first_sentence}")
            lines.append(f"   {p.url}")
        lines.append("")

    if opportunities:
        lines.append(f"Opportunities: {len(opportunities)} new")
        lines.append("")

    lines.append(f"Full report: {report_url}")
    return "\n".join(lines)


def send_email_notification(
    papers: list[SummarizedPaper],
    opportunities: list[Opportunity],
    report_url: str,
    to_email: str,
    smtp_user: str,
    smtp_password: str,
    smtp_host: str = "smtp.gmail.com",
    smtp_port: int = 587,
) -> None:
    if not smtp_user or not smtp_password or not to_email:
        return

    today = date.today().isoformat()
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Literature Guide — {today}"
    msg["From"] = smtp_user
    msg["To"] = to_email

    plain = _format_email_plain(papers, opportunities, report_url)
    html = _format_email_html(papers, opportunities, report_url)
    msg.attach(MIMEText(plain, "plain"))
    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, msg.as_string())
