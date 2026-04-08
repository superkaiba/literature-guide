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
        lines.append(f"> **[{p.title}]({p.url})** — {p.summary.split('.')[0]}.")
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
            f"**Relevance:** {p.relevance_score:.0%}"
        )
        lines.append(f"**Topics:** {', '.join(p.topics)}")
        lines.append("")
        if p.author_info:
            lines.append(f"**About the authors:** {p.author_info}")
            lines.append("")
        lines.append(f"**Summary:** {p.summary}")
        lines.append("")
        if p.reliability_assessment:
            lines.append(f"**Reliability:** {p.reliability_assessment}")
            lines.append("")
        lines.append(f"**Why it matters:** {p.why_it_matters}")
        lines.append("")
        if p.related_papers:
            lines.append("**Related papers:**")
            for rp in p.related_papers:
                url_part = f"({rp.url})" if rp.url else ""
                lines.append(
                    f"- [{rp.title}]{url_part} ({rp.year}) — {rp.summary}"
                )
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
