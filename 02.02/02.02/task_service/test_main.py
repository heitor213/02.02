from fastapi.testclient import TestClient

from main import app
from storage import storage

client = TestClient(app)


def setup_function(_):
    storage.clear()


def test_create_task_returns_201():
    r = client.post("/api/tasks", json={"title": "Купить молоко"})
    assert r.status_code == 201
    data = r.json()
    assert data["title"] == "Купить молоко"
    assert data["status"] == "new"
    assert "id" in data and "created_at" in data


def test_list_tasks():
    client.post("/api/tasks", json={"title": "A"})
    client.post("/api/tasks", json={"title": "B"})
    r = client.get("/api/tasks")
    assert r.status_code == 200
    assert len(r.json()) == 2


def test_validation_error():
    r = client.post("/api/tasks", json={"title": ""})
    assert r.status_code == 422