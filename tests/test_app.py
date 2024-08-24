from fastapi.testclient import TestClient
from web.app import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.json() == {"msg": "Welcome to this app"}
