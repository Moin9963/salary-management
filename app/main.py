from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(title="Employee Salary API")

    @app.get("/health", tags=["health"])
    def healthcheck() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
