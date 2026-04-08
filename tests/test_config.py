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
    monkeypatch.setenv("EMAIL_TO", "test@example.com")
    monkeypatch.setenv("SMTP_USER", "sender@gmail.com")
    monkeypatch.setenv("SMTP_PASSWORD", "app-password")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
    config = load_config("config.yml")
    assert config.email_to == "test@example.com"
    assert config.smtp_user == "sender@gmail.com"
    assert config.anthropic_api_key == "sk-test"


def test_load_config_max_papers():
    config = load_config("config.yml")
    assert config.max_papers == 20
