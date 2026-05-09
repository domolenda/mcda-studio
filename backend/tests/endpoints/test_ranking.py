from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_topsis_endpoint(monitor_data):
    response = client.post(
        "/ranking/topsis",
        json={
            "matrix": monitor_data["matrix"],
            "weights": monitor_data["weights"],
            "types": monitor_data["types"],
        },
    )
    assert response.status_code == 200
    assert response.json()["ranking"] == [9, 2, 1, 3, 8, 6, 7, 4, 5]


def test_topsis_invalid_weights_sum_endpoint(monitor_data):
    response = client.post(
        "/ranking/topsis",
        json={
            "matrix": monitor_data["matrix"],
            "weights": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
            "types": monitor_data["types"],
        },
    )
    assert response.status_code == 422


def test_waspas_endpoint(monitor_data):
    response = client.post(
        "/ranking/waspas",
        json={
            "matrix": monitor_data["matrix"],
            "weights": monitor_data["weights"],
            "types": monitor_data["types"],
            "lambda_": 0.5,
        },
    )
    assert response.status_code == 200
    assert response.json()["ranking"] == [9, 2, 3, 1, 8, 6, 4, 7, 5]


def test_waspas_invalid_weights_sum_endpoint(monitor_data):
    response = client.post(
        "/ranking/waspas",
        json={
            "matrix": monitor_data["matrix"],
            "weights": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
            "types": monitor_data["types"],
        },
    )
    assert response.status_code == 422


def test_vikor_endpoint(monitor_data):
    response = client.post(
        "/ranking/vikor",
        json={
            "matrix": monitor_data["matrix"],
            "weights": monitor_data["weights"],
            "types": monitor_data["types"],
            "v": 0.5,
        },
    )
    assert response.status_code == 200
    assert response.json()["ranking"] == [8, 2, 1, 3, 6, 5, 9, 4, 7]


def test_vikor_invalid_weights_sum_endpoint(monitor_data):
    response = client.post(
        "/ranking/vikor",
        json={
            "matrix": monitor_data["matrix"],
            "weights": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
            "types": monitor_data["types"],
        },
    )
    assert response.status_code == 422
