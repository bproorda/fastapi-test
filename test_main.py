from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_item():
    response = client.get("/items2/bar")
    assert response.status_code == 404  # Expecting not found initially

def test_create_item():
    response = client.post("/items/", json={"name": "bar", "description": "Bar Item", "price": "1", "tax": "0"})
    assert response.status_code == 200
    assert response.json() == {"name": "bar", "description": "Bar Item", "price": 1.0, "tax": 0.0}
