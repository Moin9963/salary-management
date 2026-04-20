from __future__ import annotations

import os
from functools import lru_cache

from pydantic import BaseModel, Field


class Settings(BaseModel):
    app_name: str = Field(default="Employee Salary API")
    environment: str = Field(default="development")
    database_url: str = Field(default="sqlite:///./employee_salary.db")
    api_host: str = Field(default="0.0.0.0")
    api_port: int = Field(default=8000)


@lru_cache
def get_settings() -> Settings:
    return Settings(
        app_name=os.getenv("APP_NAME", "Employee Salary API"),
        environment=os.getenv("ENVIRONMENT", "development"),
        database_url=os.getenv("DATABASE_URL", "sqlite:///./employee_salary.db"),
        api_host=os.getenv("API_HOST", "0.0.0.0"),
        api_port=int(os.getenv("API_PORT", "8000")),
    )
