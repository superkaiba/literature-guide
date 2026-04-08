"""Main pipeline orchestrator for the Literature Guide."""

from __future__ import annotations

import logging
from datetime import date

from src.config import load_config, Config
from src.models import RawPaper, Opportunity
from src.fetchers.arxiv_fetcher import fetch_arxiv
from src.fetchers.openalex import fetch_openalex
from src.fetchers.semantic_scholar import fetch_semantic_scholar
from src.fetchers.rss import fetch_rss
from src.fetchers.reddit import fetch_reddit
from src.fetchers.bluesky import fetch_bluesky
from src.fetchers.opportunities import fetch_opportunities
from src.dedup import deduplicate
from src.ranker import rank_papers
from src.summarizer import summarize_paper
from src.storage import save_paper
from src.report import generate_report
from src.notify import send_slack_notification

logger = logging.getLogger(__name__)


def fetch_all(config: Config) -> tuple[list[RawPaper], list[Opportunity]]:
    """Call all fetchers, catching errors so one failure doesn't stop the rest."""
    papers: list[RawPaper] = []
    opportunities: list[Opportunity] = []

    # arXiv
    try:
        papers.extend(fetch_arxiv(config.arxiv_queries))
        logger.info("arXiv: fetched %d papers", len(papers))
    except Exception:
        logger.warning("arXiv fetcher failed", exc_info=True)

    # OpenAlex
    try:
        oa = fetch_openalex(config.topics)
        papers.extend(oa)
        logger.info("OpenAlex: fetched %d papers", len(oa))
    except Exception:
        logger.warning("OpenAlex fetcher failed", exc_info=True)

    # Semantic Scholar
    try:
        s2 = fetch_semantic_scholar(
            config.topics, api_key=config.semantic_scholar_api_key
        )
        papers.extend(s2)
        logger.info("Semantic Scholar: fetched %d papers", len(s2))
    except Exception:
        logger.warning("Semantic Scholar fetcher failed", exc_info=True)

    # RSS — merge config.rss_feeds with RSS-type newsletter_sources
    try:
        all_feeds = dict(config.rss_feeds)
        for name, source in config.newsletter_sources.items():
            if source.get("type") == "rss":
                all_feeds[name] = source["url"]
        rss = fetch_rss(all_feeds)
        papers.extend(rss)
        logger.info("RSS: fetched %d papers", len(rss))
    except Exception:
        logger.warning("RSS fetcher failed", exc_info=True)

    # Reddit
    try:
        rd = fetch_reddit(config.reddit_subreddits)
        papers.extend(rd)
        logger.info("Reddit: fetched %d papers", len(rd))
    except Exception:
        logger.warning("Reddit fetcher failed", exc_info=True)

    # Bluesky
    try:
        bsky = fetch_bluesky(config.bluesky_accounts)
        papers.extend(bsky)
        logger.info("Bluesky: fetched %d papers", len(bsky))
    except Exception:
        logger.warning("Bluesky fetcher failed", exc_info=True)

    # Opportunities
    try:
        opps = fetch_opportunities(
            config.opportunity_sources, keywords=config.topics
        )
        opportunities.extend(opps)
        logger.info("Opportunities: fetched %d", len(opps))
    except Exception:
        logger.warning("Opportunities fetcher failed", exc_info=True)

    return papers, opportunities


def run_pipeline(config_path: str = "config.yml") -> None:
    """Orchestrate the full digest pipeline."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    logger.info("Starting literature digest pipeline")

    # 1. Load config
    config = load_config(config_path)
    logger.info("Loaded config with %d topics", len(config.topics))

    # 2. Fetch papers and opportunities from all sources
    raw_papers, opportunities = fetch_all(config)
    total_scanned = len(raw_papers)
    logger.info("Fetched %d raw papers and %d opportunities", len(raw_papers), len(opportunities))

    # 3. Deduplicate
    unique_papers = deduplicate(raw_papers)
    logger.info("After dedup: %d papers (removed %d duplicates)", len(unique_papers), total_scanned - len(unique_papers))

    # 4. Rank papers by relevance
    ranked = rank_papers(
        unique_papers,
        config.topics,
        api_key=config.anthropic_api_key,
        max_papers=config.max_papers,
    )
    logger.info("Ranked %d papers", len(ranked))

    # 5. Summarize each top paper
    summarized = []
    for paper, score, topics in ranked:
        try:
            sp = summarize_paper(
                paper, topics, score, api_key=config.anthropic_api_key
            )
            summarized.append(sp)
            logger.info("Summarized: %s", sp.title)
        except Exception:
            logger.warning("Failed to summarize: %s", paper.title, exc_info=True)

    # 6. Save each summarized paper
    for sp in summarized:
        try:
            save_paper(sp)
            logger.info("Saved: %s", sp.id)
        except Exception:
            logger.warning("Failed to save: %s", sp.id, exc_info=True)

    # 7. Generate daily report
    today = date.today().isoformat()
    trimmed_opportunities = opportunities[: config.max_opportunities]
    report_path = generate_report(
        summarized,
        trimmed_opportunities,
        date_str=today,
        sources_checked=7,
        papers_scanned=total_scanned,
    )
    logger.info("Report generated: %s", report_path)

    # 8. Notify via Slack
    report_url = report_path
    if config.github_repo_url:
        report_url = f"{config.github_repo_url}/blob/main/{report_path}"
    send_slack_notification(
        summarized,
        trimmed_opportunities,
        webhook_url=config.slack_webhook_url,
        report_url=report_url,
    )
    logger.info("Slack notification sent")

    logger.info("Pipeline complete — %d papers summarized", len(summarized))


if __name__ == "__main__":
    run_pipeline()
