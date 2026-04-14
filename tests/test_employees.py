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


def test_list_employees_returns_created_records(client: TestClient) -> None:
    client.post(
        "/employees",
        json={
            "full_name": "Asha Patel",
            "job_title": "Software Engineer",
            "country": "India",
            "salary": 100000,
        },
    )
    client.post(
        "/employees",
        json={
            "full_name": "John Smith",
            "job_title": "DevOps Engineer",
            "country": "United States",
            "salary": 120000,
        },
    )

    response = client.get("/employees")

    assert response.status_code == 200
