from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_navigation_maps_spanish_alias_to_anchor() -> None:
    response = client.post(
        "/api/v1/build/validate",
        json={
            "action": "navigate",
            "response": "Te llevo al Salón 101.",
            "target": "Salón 101",
            "location": "pasillo norte",
        },
    )
    payload = response.json()
    assert response.status_code == 200
    assert payload["accepted"] is True
    assert payload["target"] == "Classroom101"
    assert payload["navigation_anchor"] == "NAV_Classroom101"


def test_navigation_rejects_unknown_destination() -> None:
    response = client.post(
        "/api/v1/build/validate",
        json={
            "action": "navigate",
            "target": "Biblioteca",
        },
    )
    payload = response.json()
    assert response.status_code == 200
    assert payload["accepted"] is False
    assert payload["navigation_anchor"] is None


def test_create_chairs_maps_to_blueprint() -> None:
    response = client.post(
        "/api/v1/build/validate",
        json={
            "action": "create_object",
            "response": "Create ten chairs.",
            "object_type": "chair",
            "quantity": 10,
            "location": "Salon101",
        },
    )
    payload = response.json()
    assert response.status_code == 200
    assert payload["accepted"] is True
    assert payload["blueprint_class"] == "BP_FurnitureChair"
    assert payload["quantity"] == 10


def test_rejects_unsupported_object() -> None:
    response = client.post(
        "/api/v1/build/validate",
        json={
            "action": "create_object",
            "object_type": "spaceship",
            "quantity": 1,
        },
    )
    assert response.status_code == 200
    assert response.json()["accepted"] is False


def test_rejects_excessive_quantity() -> None:
    response = client.post(
        "/api/v1/build/validate",
        json={
            "action": "create_object",
            "object_type": "chair",
            "quantity": 101,
        },
    )
    assert response.status_code == 200
    assert response.json()["accepted"] is False


def test_delete_always_requires_confirmation() -> None:
    response = client.post(
        "/api/v1/build/validate",
        json={
            "action": "delete_object",
            "object_type": "chair",
            "quantity": 1,
        },
    )
    payload = response.json()
    assert payload["accepted"] is True
    assert payload["requires_confirmation"] is True
