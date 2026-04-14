from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db_session
from app.schemas.metrics import CountrySalaryMetrics, JobTitleSalaryMetrics
from app.services.metrics_service import (
    get_country_salary_metrics,
    get_job_title_salary_metrics,
)

router = APIRouter(prefix="/metrics/salary", tags=["metrics"])


@router.get("/country/{country}", response_model=CountrySalaryMetrics)
def country_salary_metrics(
    country: str,
    session: Session = Depends(get_db_session),
) -> CountrySalaryMetrics:
    metrics = get_country_salary_metrics(session, country)
    if metrics is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found")
    return metrics


@router.get("/job-title/{job_title}", response_model=JobTitleSalaryMetrics)
def job_title_salary_metrics(
    job_title: str,
    session: Session = Depends(get_db_session),
) -> JobTitleSalaryMetrics:
    metrics = get_job_title_salary_metrics(session, job_title)
    if metrics is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found")
    return metrics
