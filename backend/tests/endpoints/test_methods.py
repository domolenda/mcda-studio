from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_methods_ranking_endpoint():
    response = client.get("/methods/ranking")
    assert response.status_code == 200
    methods = response.json()["methods"]
    assert isinstance(methods, list)
    assert len(methods) > 0
    for method in methods:
        assert "id" in method
        assert "name" in method
        assert "normalization" in method
        assert "default_normalization" in method
        assert "parameters" in method


def test_methods_normalization_endpoint():
    response = client.get("/methods/normalization")
    assert response.status_code == 200
    normalizations = response.json()["normalizations"]
    assert isinstance(normalizations, list)
    assert len(normalizations) > 0
    for normalization in normalizations:
        assert "id" in normalization
        assert "name" in normalization
