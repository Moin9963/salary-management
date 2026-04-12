# Employee Salary API

Production-ready assessment project for employee CRUD, salary calculation, and salary metrics endpoints.

## Status

Initial scaffold only. The implementation will follow a strict TDD workflow with incremental commits.

## Planned Stack

- Python 3.11+
- FastAPI
- SQLAlchemy
- SQLite
- pytest
- Ruff

## Project Layout

```text
app/
  api/
  db/
  schemas/
  services/
  main.py
tests/
```

## Local Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
```

## Running The App

```bash
uvicorn app.main:app --reload
```

## Running Tests

```bash
pytest
```

## TDD Workflow

Each feature will be built in small Red -> Green -> Refactor cycles, with commits reflecting that flow.

## Implementation Details

This section will be expanded as the implementation progresses, including transparent notes on where AI assisted with scaffolding, test drafting, and documentation.
