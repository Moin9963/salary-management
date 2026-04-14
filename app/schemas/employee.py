from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class EmployeeCreate(BaseModel):
    full_name: str = Field(min_length=1, max_length=255)
    job_title: str = Field(min_length=1, max_length=255)
    country: str = Field(min_length=1, max_length=255)
    salary: float = Field(gt=0)


class EmployeeResponse(EmployeeCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)


class EmployeeUpdate(EmployeeCreate):
    pass
