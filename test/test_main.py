from fastapi.testclient import TestClient

from main import app


def test_main():
    # Test Client as a context tests startup and shutdown events.
    # https://fastapi.tiangolo.com/advanced/testing-events/
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200


SPP_PEAKS = [
    {"usage_kw": 996.0, "market_name": "spp", "timestamp": "2022-07-26T13:48:00"},
    {"usage_kw": 991.0, "market_name": "spp", "timestamp": "2022-07-02T10:19:54"},
    {"usage_kw": 985.0, "market_name": "spp", "timestamp": "2022-07-27T23:44:24"},
    {"usage_kw": 978.0, "market_name": "spp", "timestamp": "2022-07-06T00:43:37"},
    {"usage_kw": 977.0, "market_name": "spp", "timestamp": "2022-07-04T15:09:40"},
]


def test_read_spp_peaks():
    with TestClient(app) as client:
        response = client.get("/peaks?market_name=spp")
        assert response.status_code == 200
        assert response.json() == SPP_PEAKS
