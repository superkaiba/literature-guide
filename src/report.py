from __future__ import annotations

import os
from datetime import datetime, timezone

from src.models import SummarizedPaper, Opportunity


def generate_report(
    papers: list[SummarizedPaper],
    opportunities: list[Opportunity],
    date_str: str,
    base_dir: str = ".",
    sources_checked: int = 0,
    papers_scanned: int = 0,
) -> str:
    reports_dir = os.path.join(base_dir, "reports")
    os.makedirs(reports_dir, exist_ok=True)

    lines: list[str] = [f"# Literature Guide — {date_str}", ""]

    # Highlights
    lines.append("## Highlights")
    for p in papers[:5]:
        teaser = p.plain_language_summary.split('.')[0] if p.plain_language_summary else p.overview.split('.')[0]
        lines.append(f"> **[{p.title}]({p.url})** — {teaser}.")
    lines.append("")

    # Papers
    lines.append("## Papers")
    lines.append("")
    for i, p in enumerate(papers, 1):
        source_label = p.source.replace("_", " ").title()
        lines.append(f"### {i}. [{p.title}]({p.url})")
        lines.append(
            f"**Authors:** {', '.join(p.authors)} | "
            f"**Source:** {source_label} | "
            f"**Date:** {p.published_date} | "
            f"**Type:** {p.document_type} | "
            f"**Relevance:** {p.relevance_score:.0%}"
        )
        lines.append("")

        # Plain language summary (first!)
        if p.plain_language_summary:
            lines.append(f"**In plain English:** {p.plain_language_summary}")
            lines.append("")

        # Author info
        if p.author_info:
            lines.append(f"**About the authors:** {p.author_info}")
            lines.append("")

        # Reliability
        if p.reliability_assessment:
            lines.append(f"**Reliability:** {p.reliability_assessment}")
            lines.append("")

        # Overview
        if p.overview:
            lines.append(f"**Overview:** {p.overview}")
            lines.append("")

        # Main goal
        if p.main_goal:
            lines.append(f"**Main goal:** {p.main_goal}")
            lines.append("")

        # Key findings
        if p.key_findings:
            lines.append("**Key findings:**")
            for finding in p.key_findings:
                lines.append(f"- {finding}")
            lines.append("")

        # Methodology
        if p.methodology:
            lines.append(f"**Methodology:** {p.methodology}")
            lines.append("")

        # What's novel
        if p.distinctive_features:
            lines.append(f"**What's novel:** {p.distinctive_features}")
            lines.append("")

        # Limitations
        if p.limitations:
            lines.append(f"**Limitations:** {p.limitations}")
            lines.append("")

        # Implications
        if p.implications:
            lines.append(f"**Implications:** {p.implications}")
            lines.append("")

        # Critical assessment
        if p.critical_assessment:
            lines.append(f"**Critical assessment:** {p.critical_assessment}")
            lines.append("")

        # Key terms
        if p.key_terms:
            lines.append("**Key terms:**")
            for kt in p.key_terms:
                lines.append(f"- **{kt.term}:** {kt.definition}")
            lines.append("")

        # Related papers
        if p.related_papers:
            lines.append("**Related papers:**")
            for rp in p.related_papers:
                url_part = f"({rp.url})" if rp.url else ""
                priority_tag = f" `{rp.priority}`" if rp.priority else ""
                lines.append(
                    f"- [{rp.title}]{url_part} ({rp.year}){priority_tag} — {rp.summary}"
                )
                if rp.relevance:
                    lines.append(f"  *Why relevant: {rp.relevance}*")
            lines.append("")
        lines.extend(["---", ""])

    # Opportunities
    lines.append("## Opportunities")
    jobs = [o for o in opportunities if o.category in ("job", "fellowship")]
    cfps = [o for o in opportunities if o.category == "cfp"]
    grants = [o for o in opportunities if o.category == "grant"]
    other = [
        o
        for o in opportunities
        if o.category not in ("job", "fellowship", "cfp", "grant")
    ]
    for section_name, section_opps in [
        ("Jobs & Fellowships", jobs),
        ("Workshops & CFPs", cfps),
        ("Grants & Programs", grants),
        ("Other", other),
    ]:
        if section_opps:
            lines.append(f"### {section_name}")
            for o in section_opps:
                deadline = f", deadline: {o.deadline}" if o.deadline else ""
                lines.append(
                    f"- [{o.title}]({o.url}) — {o.organization}{deadline}"
                )
            lines.append("")

    if not opportunities:
        lines.extend(["No new opportunities found today.", ""])

    # Meta
    lines.append("## Meta")
    lines.append(f"- Sources checked: {sources_checked}")
    lines.append(f"- Papers scanned: ~{papers_scanned}")
    lines.append(
        f"- Report generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}"
    )
    lines.append("")

    report_path = os.path.join(reports_dir, f"{date_str}.md")
    with open(report_path, "w") as f:
        f.write("\n".join(lines))
    return report_path
