import responses
from src.fetchers.opportunities import fetch_opportunities
from src.models import Opportunity

@responses.activate
def test_fetch_opportunities_returns_list():
    responses.add(responses.GET, "https://jobs.80000hours.org/jobs", body="<html></html>", status=200)
    opps = fetch_opportunities(
        {"eighty_thousand_hours": "https://jobs.80000hours.org/jobs"},
        keywords=["safety", "alignment", "interpretability"],
    )
    assert isinstance(opps, list)
    for opp in opps:
        assert isinstance(opp, Opportunity)
