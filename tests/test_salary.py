from __future__ import annotations

from fastapi.testclient import TestClient


def test_salary_calculation_for_india(client: TestClient) -> None:
    create_response = client.post(
        "/employees",
        json={
            "full_name": "Asha Patel",
            "job_title": "Software Engineer",
            "country": "India",
            "salary": 100000,
        },
    )

    response = client.get(f"/employees/{create_response.json()['id']}/salary")

    assert response.status_code == 200
