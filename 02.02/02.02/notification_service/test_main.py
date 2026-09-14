from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def _valid_body():
    return {
        "event": "task_created",
        "payload": {
            "id": "00000000-0000-0000-0000-000000000001",
            "title": "Test",
            "description": None,
            "status": "new",
            "created_at": "2026-09-14T10:00:00Z",
        },
    }


def test_webhook_ok():
    r = client.post("/api/webhooks/task_created", json=_valid_body())
    assert r.status_code == 200
    assert r.json() == {"status": "received"}


def test_webhook_bad_payload():
    r = client.post("/api/webhooks/task_created", json={"event": "x"})
    assert r.status_code == 422