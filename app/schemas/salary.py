from __future__ import annotations

from pydantic import BaseModel


class SalaryBreakdown(BaseModel):
    employee_id: int
    country: str
    gross_salary: float
    deduction_rate: float
    deduction_amount: float
    net_salary: float
