import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_predict_price():
    payload = {"asset_symbol": "BTC", "days": 30}

    response = client.post("/api/v1/predictions/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "predicted_price" in data
    assert "confidence_interval" in data


def test_get_prediction_history():
    response = client.get("/api/v1/predictions/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
