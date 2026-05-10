from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_run_entropy_weights(monitor_data):
    response = client.post("/weights/entropy", json={"matrix": monitor_data["matrix"]})
    assert response.status_code == 200


def test_run_entropy_weights_empty_matrix():
    response = client.post("/weights/entropy", json={"matrix": []})
    assert response.status_code == 422


def test_run_equal_weights(monitor_data):
    response = client.post("/weights/equal", json={"matrix": monitor_data["matrix"]})
    assert response.status_code == 200


def test_run_equal_weights_empty_matrix():
    response = client.post("/weights/equal", json={"matrix": []})
    assert response.status_code == 422
