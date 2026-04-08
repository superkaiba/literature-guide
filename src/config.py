from __future__ import annotations

import os
from dataclasses import dataclass, field

import yaml


@dataclass
class Config:
    topics: list[str]
    arxiv_queries: list[str]
    rss_feeds: dict[str, str]
    reddit_subreddits: list[str]
    bluesky_accounts: list[str]
    newsletter_sources: dict[str, dict]
    opportunity_sources: dict[str, str]
    max_papers: int = 20
    max_opportunities: int = 10
    github_repo_url: str = ""
    email_to: str = ""
    smtp_user: str = ""
    smtp_password: str = ""
    anthropic_api_key: str = ""
    semantic_scholar_api_key: str = ""


def load_config(path: str = "config.yml") -> Config:
    with open(path) as f:
        raw = yaml.safe_load(f)

    return Config(
        topics=raw["topics"],
        arxiv_queries=raw["arxiv_queries"],
        rss_feeds=raw["rss_feeds"],
        reddit_subreddits=raw["reddit_subreddits"],
        bluesky_accounts=raw["bluesky_accounts"],
        newsletter_sources=raw["newsletter_sources"],
        opportunity_sources=raw["opportunity_sources"],
        max_papers=raw.get("max_papers", 20),
        max_opportunities=raw.get("max_opportunities", 10),
        github_repo_url=raw.get("github_repo_url", ""),
        email_to=os.environ.get("EMAIL_TO", ""),
        smtp_user=os.environ.get("SMTP_USER", ""),
        smtp_password=os.environ.get("SMTP_PASSWORD", ""),
        anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY", ""),
        semantic_scholar_api_key=os.environ.get("SEMANTIC_SCHOLAR_API_KEY", ""),
    )
