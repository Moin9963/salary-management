from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import Employee
from app.db.session import get_db_session
from app.schemas.employee import EmployeeCreate, EmployeeResponse, EmployeeUpdate

router = APIRouter(prefix="/employees", tags=["employees"])


@router.post("", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(
    payload: EmployeeCreate,
    session: Session = Depends(get_db_session),
) -> Employee:
    employee = Employee(**payload.model_dump())
    session.add(employee)
    session.commit()
    session.refresh(employee)
    return employee


@router.get("", response_model=list[EmployeeResponse])
def list_employees(session: Session = Depends(get_db_session)) -> list[Employee]:
    statement = select(Employee).order_by(Employee.id)
    return list(session.scalars(statement).all())


@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int, session: Session = Depends(get_db_session)) -> Employee:
    employee = session.get(Employee, employee_id)
    if employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return employee


@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    payload: EmployeeUpdate,
    session: Session = Depends(get_db_session),
) -> Employee:
    employee = session.get(Employee, employee_id)
    if employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")

    for field, value in payload.model_dump().items():
        setattr(employee, field, value)

    session.add(employee)
    session.commit()
    session.refresh(employee)
    return employee
