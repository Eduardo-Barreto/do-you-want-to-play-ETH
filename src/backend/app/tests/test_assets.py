import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.asset import Asset

client = TestClient(app)


@pytest.fixture(scope="module")
def test_asset():
    return Asset(name="Bitcoin", symbol="BTC", current_price=30000.00)


def test_create_asset(test_asset):
    response = client.post("/api/v1/assets/", json=test_asset.dict())
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == test_asset.name
    assert data["symbol"] == test_asset.symbol


def test_read_assets():
    response = client.get("/api/v1/assets/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_read_asset(test_asset):
    response = client.get(f"/api/v1/assets/{test_asset.symbol}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_asset.name
    assert data["symbol"] == test_asset.symbol


def test_update_asset(test_asset):
    update_data = {"name": "Bitcoin Updated", "current_price": 32000.00}
    response = client.put(f"/api/v1/assets/{test_asset.symbol}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_data["name"]


def test_delete_asset(test_asset):
    response = client.delete(f"/api/v1/assets/{test_asset.symbol}")
    assert response.status_code == 204
