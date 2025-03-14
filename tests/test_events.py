import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def sample_event():
    return {
        "name": "Sample Event",
        "date": "2025-03-15T15:00:00",
        "description": "A test event",
        "visibility": "public",
        "location": "Campus Auditorium",
        "link": "https://event-link.com"
    }

def test_create_event(sample_event):
    response = client.post("/events/", json=sample_event)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["message"] == "Event created successfully"

def test_get_events():
    response = client.get("/events/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)  # Should return a list of events

def test_filter_events_by_visibility():
    response = client.get("/events/?visibility=public")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for event in data:
        assert event["visibility"] == "public"

def test_filter_events_by_time():
    response = client.get("/events/?start_time=2025-01-01T00:00:00&end_time=2025-12-31T23:59:59")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
