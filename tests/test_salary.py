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
    assert response.json() == {
        "employee_id": 1,
        "country": "India",
        "gross_salary": 100000.0,
        "deduction_rate": 0.1,
        "deduction_amount": 10000.0,
        "net_salary": 90000.0,
    }


def test_salary_calculation_for_united_states(client: TestClient) -> None:
    create_response = client.post(
        "/employees",
        json={
            "full_name": "John Smith",
            "job_title": "DevOps Engineer",
            "country": "United States",
            "salary": 120000,
        },
    )

    response = client.get(f"/employees/{create_response.json()['id']}/salary")

    assert response.status_code == 200
    assert response.json()["deduction_rate"] == 0.12
    assert response.json()["deduction_amount"] == 14400.0
    assert response.json()["net_salary"] == 105600.0


def test_salary_calculation_for_other_country_has_no_deduction(client: TestClient) -> None:
    create_response = client.post(
        "/employees",
        json={
            "full_name": "Maria Garcia",
            "job_title": "QA Engineer",
            "country": "Spain",
            "salary": 80000,
        },
    )

    response = client.get(f"/employees/{create_response.json()['id']}/salary")

    assert response.status_code == 200
    assert response.json()["deduction_rate"] == 0.0
