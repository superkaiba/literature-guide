from src.dedup import deduplicate
from src.models import RawPaper


def _paper(title="Test Paper", doi=None, url="https://example.com/1", source="arxiv"):
    return RawPaper(
        title=title,
        authors=["A"],
        abstract="Abstract",
        url=url,
        source=source,
        published_date="2026-04-06",
        doi=doi,
        tags=[],
    )


def test_dedup_by_doi():
    papers = [
        _paper(title="Paper A", doi="10.1234/test", source="arxiv"),
        _paper(title="Paper A (preprint)", doi="10.1234/test", source="openalex"),
    ]
    result = deduplicate(papers)
    assert len(result) == 1


def test_dedup_by_fuzzy_title():
    papers = [
        _paper(
            title="Sparse Autoencoders Find Interpretable Features",
            source="arxiv",
        ),
        _paper(
            title="Sparse Autoencoders Find Interpretable Features in LLMs",
            source="openalex",
            url="https://example.com/2",
        ),
    ]
    result = deduplicate(papers)
    assert len(result) == 1


def test_dedup_keeps_different_papers():
    papers = [
        _paper(title="Paper About Safety", url="https://example.com/1"),
        _paper(title="Paper About Alignment", url="https://example.com/2"),
    ]
    result = deduplicate(papers)
    assert len(result) == 2


def test_dedup_prefers_arxiv_source():
    papers = [
        _paper(title="Same Paper", doi="10.1234/x", source="openalex"),
        _paper(title="Same Paper", doi="10.1234/x", source="arxiv"),
    ]
    result = deduplicate(papers)
    assert len(result) == 1
    assert result[0].source == "arxiv"
