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
        "<html><body style='font-family: Georgia, serif; max-width: 800px; margin: 0 auto; color: #1a1a1a;'>",
        f"<h1 style='border-bottom: 2px solid #333;'>Literature Guide &mdash; {today}</h1>",
        f"<p>{len(papers)} papers curated today. "
        f'<a href="{report_url}">Full report on GitHub</a></p>',
    ]

    for i, p in enumerate(papers, 1):
        source_label = p.source.replace("_", " ").title()
        lines.append("<div style='margin-bottom: 2em; padding: 1em; background: #f9f9f9; border-left: 4px solid #2563eb;'>")
        lines.append(f"<h2 style='margin-top: 0;'>{i}. <a href=\"{p.url}\">{p.title}</a></h2>")
        lines.append(
            f"<p style='color: #666; font-size: 0.9em;'>"
            f"<strong>Authors:</strong> {', '.join(p.authors)} &middot; "
            f"<strong>Source:</strong> {source_label} &middot; "
            f"<strong>Date:</strong> {p.published_date} &middot; "
            f"<strong>Type:</strong> {p.document_type} &middot; "
            f"<strong>Relevance:</strong> {p.relevance_score:.0%}</p>"
        )

        # Author info
        if p.author_info:
            lines.append(f"<p style='color: #555; font-style: italic;'>{p.author_info}</p>")

        # Reliability badge
        if p.reliability_assessment:
            color = "#16a34a" if "HIGH" in p.reliability_assessment else "#d97706" if "MEDIUM" in p.reliability_assessment else "#dc2626"
            lines.append(f"<p><span style='background: {color}; color: white; padding: 2px 8px; border-radius: 3px; font-size: 0.85em;'>{p.reliability_assessment.split('.')[0]}</span></p>")

        # Overview
        if p.overview:
            lines.append(f"<p><strong>Overview:</strong> {p.overview}</p>")

        # Main goal
        if p.main_goal:
            lines.append(f"<p><strong>Goal:</strong> {p.main_goal}</p>")

        # Key findings
        if p.key_findings:
            lines.append("<p><strong>Key findings:</strong></p><ul>")
            for f_ in p.key_findings:
                lines.append(f"<li>{f_}</li>")
            lines.append("</ul>")

        # Methodology
        if p.methodology:
            lines.append(f"<p><strong>Methodology:</strong> {p.methodology}</p>")

        # What's novel
        if p.distinctive_features:
            lines.append(f"<p><strong>What's novel:</strong> {p.distinctive_features}</p>")

        # Implications
        if p.implications:
            lines.append(f"<p><strong>Implications:</strong> {p.implications}</p>")

        # Limitations
        if p.limitations:
            lines.append(f"<details><summary><strong>Limitations & open questions</strong></summary><p>{p.limitations}</p></details>")

        # Critical assessment
        if p.critical_assessment:
            lines.append(f"<details><summary><strong>Critical assessment</strong></summary><p>{p.critical_assessment}</p></details>")

        # Key terms
        if p.key_terms:
            terms_html = ", ".join(f"<strong>{kt.term}</strong>: {kt.definition}" for kt in p.key_terms)
            lines.append(f"<details><summary><strong>Key terms</strong></summary><p>{terms_html}</p></details>")

        # Related papers
        if p.related_papers:
            lines.append("<p><strong>Related work:</strong></p><ul>")
            for rp in p.related_papers:
                priority_badge = ""
                if rp.priority:
                    pcolor = "#dc2626" if rp.priority == "Essential" else "#d97706" if rp.priority == "Recommended" else "#6b7280"
                    priority_badge = f" <span style='background: {pcolor}; color: white; padding: 1px 5px; border-radius: 2px; font-size: 0.75em;'>{rp.priority}</span>"
                if rp.url:
                    lines.append(f'<li><a href="{rp.url}">{rp.title}</a> ({rp.year}){priority_badge} &mdash; {rp.summary}')
                else:
                    lines.append(f"<li>{rp.title} ({rp.year}){priority_badge} &mdash; {rp.summary}")
                if rp.relevance:
                    lines.append(f"<br><em style='color: #666; font-size: 0.85em;'>Why: {rp.relevance}</em>")
                lines.append("</li>")
            lines.append("</ul>")

        lines.append("</div>")

    # Opportunities
    if opportunities:
        lines.append("<h2>Opportunities</h2><ul>")
        for o in opportunities:
            deadline = f" (deadline: {o.deadline})" if o.deadline else ""
            lines.append(
                f'<li><a href="{o.url}">{o.title}</a> &mdash; {o.organization}{deadline}</li>'
            )
        lines.append("</ul>")

    lines.append(f'<p style="margin-top: 2em; border-top: 1px solid #ccc; padding-top: 1em;"><a href="{report_url}">Full report on GitHub</a></p>')
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
        lines.append(f"   Source: {source_label} | Date: {p.published_date} | Type: {p.document_type}")
        lines.append(f"   URL: {p.url}")
        if p.author_info:
            lines.append(f"   Authors: {p.author_info}")
        if p.reliability_assessment:
            lines.append(f"   Reliability: {p.reliability_assessment}")
        if p.overview:
            lines.append(f"   Overview: {p.overview}")
        if p.main_goal:
            lines.append(f"   Goal: {p.main_goal}")
        if p.key_findings:
            lines.append("   Key findings:")
            for f_ in p.key_findings:
                lines.append(f"   - {f_}")
        if p.methodology:
            lines.append(f"   Methodology: {p.methodology}")
        if p.distinctive_features:
            lines.append(f"   Novel: {p.distinctive_features}")
        if p.implications:
            lines.append(f"   Implications: {p.implications}")
        if p.related_papers:
            lines.append("   Related:")
            for rp in p.related_papers:
                priority = f" [{rp.priority}]" if rp.priority else ""
                lines.append(f"   - {rp.title} ({rp.year}){priority}: {rp.summary}")
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
