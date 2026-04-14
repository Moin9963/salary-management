from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class EmployeeBase(BaseModel):
    full_name: str = Field(min_length=1, max_length=255)
    job_title: str = Field(min_length=1, max_length=255)
    country: str = Field(min_length=1, max_length=255)
    salary: float = Field(gt=0)


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
