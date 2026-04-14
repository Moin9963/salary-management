from fastapi import FastAPI

from app.api.employees import router as employees_router
from app.api.metrics import router as metrics_router
from app.api.salary import router as salary_router
from app.db import models  # noqa: F401
from app.db.session import Base, engine


def create_app() -> FastAPI:
    app = FastAPI(title="Employee Salary API")
    Base.metadata.create_all(bind=engine)
    app.include_router(employees_router)
    app.include_router(metrics_router)
    app.include_router(salary_router)

    @app.get("/health", tags=["health"])
    def healthcheck() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
