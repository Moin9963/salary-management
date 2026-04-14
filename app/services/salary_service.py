from __future__ import annotations

from app.db.models import Employee
from app.schemas.salary import SalaryBreakdown


def calculate_salary_breakdown(employee: Employee) -> SalaryBreakdown:
    deduction_rate = 0.10 if employee.country.strip().lower() == "india" else 0.0
    deduction_amount = round(employee.salary * deduction_rate, 2)
    net_salary = round(employee.salary - deduction_amount, 2)

    return SalaryBreakdown(
        employee_id=employee.id,
        country=employee.country,
        gross_salary=employee.salary,
        deduction_rate=deduction_rate,
        deduction_amount=deduction_amount,
        net_salary=net_salary,
    )
