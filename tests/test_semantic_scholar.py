import responses
from src.fetchers.semantic_scholar import fetch_semantic_scholar

SAMPLE_RESPONSE = {
    "data": [{
        "paperId": "abc123", "title": "Alignment Faking in LLMs",
        "authors": [{"name": "Alice"}, {"name": "Bob"}],
        "abstract": "We demonstrate alignment faking.",
        "url": "https://www.semanticscholar.org/paper/abc123",
        "externalIds": {"DOI": "10.1234/test"},
        "publicationDate": "2026-04-06", "fieldsOfStudy": ["Computer Science"],
    }]
}

@responses.activate
def test_fetch_semantic_scholar():
    responses.add(responses.GET, "https://api.semanticscholar.org/graph/v1/paper/search", json=SAMPLE_RESPONSE, status=200)
    papers = fetch_semantic_scholar(["alignment faking"], api_key="test-key")
    assert len(papers) == 1
    assert papers[0].source == "semantic_scholar"
