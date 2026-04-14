from __future__ import annotations

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.db.models import Employee
from app.schemas.metrics import CountrySalaryMetrics, JobTitleSalaryMetrics


def get_country_salary_metrics(session: Session, country: str) -> CountrySalaryMetrics | None:
    statement = select(
        func.min(Employee.salary),
        func.max(Employee.salary),
        func.avg(Employee.salary),
    ).where(Employee.country == country)
    min_salary, max_salary, avg_salary = session.execute(statement).one()

    if min_salary is None or max_salary is None or avg_salary is None:
        return None

    return CountrySalaryMetrics(
        country=country,
        min_salary=round(min_salary, 2),
        max_salary=round(max_salary, 2),
        avg_salary=round(avg_salary, 2),
    )


def get_job_title_salary_metrics(session: Session, job_title: str) -> JobTitleSalaryMetrics | None:
    statement = select(func.avg(Employee.salary)).where(Employee.job_title == job_title)
    avg_salary = session.execute(statement).scalar_one()

    if avg_salary is None:
        return None

    return JobTitleSalaryMetrics(job_title=job_title, avg_salary=round(avg_salary, 2))
