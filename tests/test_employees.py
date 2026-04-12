from __future__ import annotations

from fastapi.testclient import TestClient


def test_create_employee_returns_201(client: TestClient) -> None:
    response = client.post(
        "/employees",
        json={
            "full_name": "Asha Patel",
            "job_title": "Software Engineer",
            "country": "India",
            "salary": 100000,
        },
    )

    assert response.status_code == 201
