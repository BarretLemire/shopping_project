import pytest
from fastapi.testclient import TestClient
from main import app
from sqlalchemy.orm import Session
from database_operations import get_db
from models import Item

# Fixture to create a test database session
@pytest.fixture(scope="module")
def test_db():
    db = next(get_db())
    yield db
    db.close()

# Fixture to create a test client for the FastAPI app
@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    return client

# Test case to ensure that the "/items/" endpoint returns a 200 OK status code
def test_get_items(test_client: TestClient):
    response = test_client.get("/items")
    assert response.status_code == 200

# Test case to ensure that the "/items/" endpoint returns a list of items
def test_get_items_list(test_client: TestClient, test_db: Session):
    response = test_client.get("/items")
    assert response.json() == []

# Test case to ensure that the "/items/" endpoint can successfully create a new item
def test_create_item(test_client: TestClient, test_db: Session):
    new_item_data = {
        "name": "Test Item",
        "quantity": 10,
        "type": "Test Type",
        "brand": "Test Brand",
        "color": "Test Color",
        "price": 100.0
    }
    response = test_client.post("/items/", json=new_item_data)
    assert response.status_code == 200
    created_item = response.json()
    assert created_item["name"] == new_item_data["name"]
    assert created_item["quantity"] == new_item_data["quantity"]
    assert created_item["type"] == new_item_data["type"]
    assert created_item["brand"] == new_item_data["brand"]
    assert created_item["color"] == new_item_data["color"]
    assert created_item["price"] == new_item_data["price"]

# Test case to ensure that the "/total_cost" endpoint returns a 200 OK status code
def test_get_total_cost(test_client: TestClient):
    response = test_client.get("/total_cost")
    assert response.status_code == 200

# Test case to ensure that the "/total_cost" endpoint returns a valid JSON response
def test_get_total_cost_response(test_client: TestClient):
    response = test_client.get("/total_cost")
    assert "total_cost" in response.json()


