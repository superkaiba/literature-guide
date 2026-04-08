import responses
from src.fetchers.openalex import fetch_openalex
from src.models import RawPaper

SAMPLE_RESPONSE = {
    "results": [{
        "title": "Sparse Autoencoders for Interpretability",
        "authorships": [{"author": {"display_name": "Alice Smith"}}, {"author": {"display_name": "Bob Jones"}}],
        "abstract_inverted_index": {"We": [0], "study": [1], "sparse": [2], "autoencoders": [3], "for": [4], "interpretability.": [5]},
        "doi": "https://doi.org/10.1234/test",
        "id": "https://openalex.org/W123",
        "publication_date": "2026-04-06",
        "topics": [{"display_name": "Machine Learning"}],
    }]
}

@responses.activate
def test_fetch_openalex_returns_papers():
    responses.add(responses.GET, "https://api.openalex.org/works", json=SAMPLE_RESPONSE, status=200)
    papers = fetch_openalex(["mechanistic interpretability"])
    assert len(papers) == 1
    assert isinstance(papers[0], RawPaper)
    assert papers[0].source == "openalex"
    assert "We study sparse autoencoders for interpretability." in papers[0].abstract
