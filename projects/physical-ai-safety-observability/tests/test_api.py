from fastapi.testclient import TestClient

from api.main import app
from api.services.store import store
from events.schemas import SafetyEvent
from edge.source_loader import load_json


def test_health_endpoint() -> None:
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_event_ingestion_creates_incident() -> None:
    store.reset()
    client = TestClient(app)
    payload = load_json("examples/sample_event.json")

    response = client.post("/events", json=payload)

    assert response.status_code == 200
    event = SafetyEvent.model_validate(response.json())
    incidents = client.get("/incidents").json()
    assert event.rule_id == "PPE_MISSING"
    assert incidents[0]["incident_id"] == "cell-a-camera-1:PPE_MISSING"
    assert incidents[0]["event_ids"] == ["sample-event-1"]

