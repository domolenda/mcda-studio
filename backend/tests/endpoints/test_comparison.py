from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_comparison_endpoint(monitor_data):
    response = client.post(
        "/comparison",
        json={
            "matrix": monitor_data["matrix"],
            "weights": monitor_data["weights"],
            "types": monitor_data["types"],
            "methods_config": [
                {
                    "name": "topsis",
                    "params": [{"name": "normalization_method", "value": "min_max"}],
                },
                {
                    "name": "waspas",
                    "params": [
                        {"name": "normalization_method", "value": "linear"},
                        {"name": "lambda_", "value": 0.5},
                    ],
                },
            ],
        },
    )
    assert response.status_code == 200
    assert "rankings" in response.json()
    assert "correlations" in response.json()
    assert "topsis" in response.json()["rankings"]
    assert "waspas" in response.json()["rankings"]


def test_comparison_single_method(monitor_data):
    response = client.post(
        "/comparison",
        json={
            "matrix": monitor_data["matrix"],
            "weights": monitor_data["weights"],
            "types": monitor_data["types"],
            "methods_config": [
                {
                    "name": "topsis",
                    "params": [{"name": "normalization_method", "value": "min_max"}],
                }
            ],
        },
    )
    assert response.status_code == 422
