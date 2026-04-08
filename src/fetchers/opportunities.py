from __future__ import annotations
import re
import requests
from src.models import Opportunity


def _scrape_80k_hours(url: str, keywords: list[str]) -> list[Opportunity]:
    resp = requests.get(
        url, headers={"User-Agent": "literature-guide/1.0"}, timeout=30
    )
    if resp.status_code != 200:
        return []
    opps: list[Opportunity] = []
    title_pattern = re.compile(
        r'class="[^"]*job[_-]?title[^"]*"[^>]*>([^<]+)', re.I
    )
    org_pattern = re.compile(
        r'class="[^"]*organi[sz]ation[^"]*"[^>]*>([^<]+)', re.I
    )
    link_pattern = re.compile(r'href="(/job[^"]*)"', re.I)
    titles = title_pattern.findall(resp.text)
    orgs = org_pattern.findall(resp.text)
    links = link_pattern.findall(resp.text)
    for i, title in enumerate(titles):
        if not any(kw.lower() in title.lower() for kw in keywords):
            continue
        org = orgs[i] if i < len(orgs) else ""
        link = links[i] if i < len(links) else ""
        full_url = (
            f"https://jobs.80000hours.org{link}"
            if link.startswith("/")
            else link
        )
        opps.append(
            Opportunity(
                title=title.strip(),
                url=full_url,
                organization=org.strip(),
                category="job",
            )
        )
    return opps


def fetch_opportunities(
    sources: dict[str, str], keywords: list[str] | None = None
) -> list[Opportunity]:
    keywords = keywords or [
        "safety",
        "alignment",
        "interpretability",
        "mechanistic",
    ]
    opps: list[Opportunity] = []
    for source_name, url in sources.items():
        if "80000hours" in source_name:
            opps.extend(_scrape_80k_hours(url, keywords))
        else:
            try:
                resp = requests.get(
                    url,
                    headers={"User-Agent": "literature-guide/1.0"},
                    timeout=30,
                )
                if resp.status_code != 200:
                    continue
                link_re = re.compile(
                    r'<a[^>]+href="([^"]+)"[^>]*>([^<]+)</a>', re.I
                )
                for href, text in link_re.findall(resp.text):
                    if any(kw.lower() in text.lower() for kw in keywords):
                        opps.append(
                            Opportunity(
                                title=text.strip(),
                                url=href
                                if href.startswith("http")
                                else f"{url.rstrip('/')}/{href.lstrip('/')}",
                                organization=source_name,
                                category="job",
                            )
                        )
            except requests.RequestException:
                continue
    return opps
