from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.models import Employee
from app.db.session import get_db_session
from app.schemas.salary import SalaryBreakdown
from app.services.salary_service import calculate_salary_breakdown

router = APIRouter(tags=["salary"])


@router.get("/employees/{employee_id}/salary", response_model=SalaryBreakdown)
def get_salary_breakdown(
    employee_id: int,
    session: Session = Depends(get_db_session),
) -> SalaryBreakdown:
    employee = session.get(Employee, employee_id)
    if employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return calculate_salary_breakdown(employee)
