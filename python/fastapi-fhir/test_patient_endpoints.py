from collections.abc import Mapping
from copy import deepcopy
from typing import Any

import pytest


from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


@pytest.fixture(scope="session")
def patient_message() -> dict[str, Any]:
    return {
        "id": "1",
        "active": True,
        "name": {"example": "example"},
        "gender": "U",
        "birthDate": "01-18-2024",
        "telecom": {"phone": "1111111111"},
    }


def test_create__success(patient_message: Mapping[str, Any]):
    response = client.post("/Patient/", json=patient_message)
    assert response.status_code == 200
    assert response.json() == patient_message


def test_read_patient__success():
    response = client.get("/Patient/1")
    assert response.status_code == 200
    assert response.json() == {"msg": "read resource for 1"}


def test_update__success(patient_message: dict[str, Any]):
    updated_patient_message = deepcopy(patient_message)
    updated_patient_message["birthDate"] = "2024-01-21"
    response = client.put("/Patient/1", json=updated_patient_message)
    assert response.status_code == 200
    assert response.json() == {"msg": "the updated resource for 1"}


def test_search__success():
    response = client.get("/Patient")
    assert response.status_code == 200
    assert response.json() == {"msg": "a patient search bundle"}
