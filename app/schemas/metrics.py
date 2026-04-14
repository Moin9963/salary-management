from __future__ import annotations

from pydantic import BaseModel


class CountrySalaryMetrics(BaseModel):
    country: str
    min_salary: float
    max_salary: float
    avg_salary: float


class JobTitleSalaryMetrics(BaseModel):
    job_title: str
    avg_salary: float
