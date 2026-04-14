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


def test_get_employee_by_id_returns_employee(client: TestClient) -> None:
    create_response = client.post(
        "/employees",
        json={
            "full_name": "Maria Garcia",
            "job_title": "QA Engineer",
            "country": "Spain",
            "salary": 80000,
        },
    )

    response = client.get(f"/employees/{create_response.json()['id']}")

    assert response.status_code == 200


def test_get_unknown_employee_returns_404(client: TestClient) -> None:
    response = client.get("/employees/999")

    assert response.status_code == 404


def test_update_employee_returns_200(client: TestClient) -> None:
    create_response = client.post(
        "/employees",
        json={
            "full_name": "Maria Garcia",
            "job_title": "QA Engineer",
            "country": "Spain",
            "salary": 80000,
        },
    )

    response = client.put(
        f"/employees/{create_response.json()['id']}",
        json={
            "full_name": "Maria Garcia",
            "job_title": "Senior QA Engineer",
            "country": "Spain",
            "salary": 90000,
        },
    )

    assert response.status_code == 200
    assert response.json()["job_title"] == "Senior QA Engineer"
    assert response.json()["salary"] == 90000.0


def test_delete_employee_returns_204(client: TestClient) -> None:
    create_response = client.post(
        "/employees",
        json={
            "full_name": "Lina Chen",
            "job_title": "Data Analyst",
            "country": "Singapore",
            "salary": 95000,
        },
    )

    response = client.delete(f"/employees/{create_response.json()['id']}")

    assert response.status_code == 204
