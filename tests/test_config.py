import os
from src.config import load_config


def test_load_config_reads_topics():
    config = load_config("config.yml")
    assert "mechanistic interpretability" in config.topics


def test_load_config_reads_rss_feeds():
    config = load_config("config.yml")
    assert "alignment_forum" in config.rss_feeds
    assert config.rss_feeds["alignment_forum"].startswith("http")


def test_load_config_reads_env_overrides(monkeypatch):
    monkeypatch.setenv("SLACK_WEBHOOK_URL", "https://hooks.slack.com/test")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
    config = load_config("config.yml")
    assert config.slack_webhook_url == "https://hooks.slack.com/test"
    assert config.anthropic_api_key == "sk-test"


def test_load_config_max_papers():
    config = load_config("config.yml")
    assert config.max_papers == 20
