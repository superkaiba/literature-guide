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
        "<html><body>",
        f"<h2>Literature Guide &mdash; {today}</h2>",
        f"<p>{len(papers)} papers curated today. "
        f'<a href="{report_url}">Full report on GitHub</a></p>',
        "<hr>",
    ]

    for i, p in enumerate(papers, 1):
        source_label = p.source.replace("_", " ").title()
        lines.append(f"<h3>{i}. <a href=\"{p.url}\">{p.title}</a></h3>")
        lines.append(
            f"<p><strong>Authors:</strong> {', '.join(p.authors)}<br>"
            f"<strong>Source:</strong> {source_label} &middot; "
            f"<strong>Date:</strong> {p.published_date} &middot; "
            f"<strong>Relevance:</strong> {p.relevance_score:.0%}</p>"
        )
        if p.author_info:
            lines.append(
                f"<p><em>{p.author_info}</em></p>"
            )
        lines.append(f"<p>{p.summary}</p>")
        if p.reliability_assessment:
            lines.append(
                f"<p><strong>Reliability:</strong> {p.reliability_assessment}</p>"
            )
        lines.append(f"<p><strong>Why it matters:</strong> {p.why_it_matters}</p>")
        if p.related_papers:
            lines.append("<p><strong>Related work:</strong></p><ul>")
            for rp in p.related_papers:
                if rp.url:
                    lines.append(
                        f'<li><a href="{rp.url}">{rp.title}</a> ({rp.year}) &mdash; {rp.summary}</li>'
                    )
                else:
                    lines.append(
                        f"<li>{rp.title} ({rp.year}) &mdash; {rp.summary}</li>"
                    )
            lines.append("</ul>")
        lines.append("<hr>")

    if opportunities:
        lines.append("<h3>Opportunities</h3><ul>")
        for o in opportunities:
            deadline = f" (deadline: {o.deadline})" if o.deadline else ""
            lines.append(
                f'<li><a href="{o.url}">{o.title}</a> &mdash; {o.organization}{deadline}</li>'
            )
        lines.append("</ul>")

    lines.append(f'<p><a href="{report_url}">Full report on GitHub</a></p>')
    lines.append("</body></html>")
    return "\n".join(lines)


def _format_email_plain(
    papers: list[SummarizedPaper],
    opportunities: list[Opportunity],
    report_url: str,
) -> str:
    today = date.today().isoformat()
    lines = [f"Literature Guide — {today}", "=" * 40, ""]

    for i, p in enumerate(papers, 1):
        source_label = p.source.replace("_", " ").title()
        lines.append(f"{i}. {p.title}")
        lines.append(f"   Authors: {', '.join(p.authors)}")
        lines.append(f"   Source: {source_label} | Date: {p.published_date}")
        lines.append(f"   URL: {p.url}")
        if p.author_info:
            lines.append(f"   Who: {p.author_info}")
        lines.append(f"   {p.summary}")
        if p.reliability_assessment:
            lines.append(f"   Reliability: {p.reliability_assessment}")
        lines.append(f"   Why it matters: {p.why_it_matters}")
        if p.related_papers:
            lines.append("   Related:")
            for rp in p.related_papers:
                lines.append(f"   - {rp.title} ({rp.year}): {rp.summary}")
        lines.append("")

    if opportunities:
        lines.append("OPPORTUNITIES")
        lines.append("-" * 20)
        for o in opportunities:
            deadline = f" (deadline: {o.deadline})" if o.deadline else ""
            lines.append(f"- {o.title} — {o.organization}{deadline}")
            lines.append(f"  {o.url}")
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
    paper_count = len(papers)
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Literature Guide — {today} ({paper_count} papers)"
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
