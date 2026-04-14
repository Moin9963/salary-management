from __future__ import annotations

from fastapi.testclient import TestClient


def seed_metrics_data(client: TestClient) -> None:
    employees = [
        {
            "full_name": "Asha Patel",
            "job_title": "Software Engineer",
            "country": "India",
            "salary": 100000,
        },
        {
            "full_name": "Raj Kumar",
            "job_title": "Software Engineer",
            "country": "India",
            "salary": 150000,
        },
    ]

    for employee in employees:
        client.post("/employees", json=employee)


def test_country_salary_metrics_returns_200(client: TestClient) -> None:
    seed_metrics_data(client)

    response = client.get("/metrics/salary/country/India")

    assert response.status_code == 200
    assert response.json() == {
        "country": "India",
        "min_salary": 100000.0,
        "max_salary": 150000.0,
        "avg_salary": 125000.0,
    }
