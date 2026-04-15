# Employee Salary API

Production-ready assessment project for employee CRUD, salary calculation, and salary metrics endpoints.

## Status

Implemented with a granular 46-commit history that shows the feature growth from scaffold to CRUD, salary calculation, salary metrics, and test coverage.

## Stack

- Python 3.11+
- FastAPI
- Pydantic
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
python -m pip install -e .[dev]
```

## Running The App

```bash
python -m uvicorn app.main:app --reload
```

## Running Tests

```bash
python -m pytest
```

## API Endpoints

- `POST /employees`
- `GET /employees`
- `GET /employees/{employee_id}`
- `PUT /employees/{employee_id}`
- `DELETE /employees/{employee_id}`
- `GET /employees/{employee_id}/salary`
- `GET /metrics/salary/country/{country}`
- `GET /metrics/salary/job-title/{job_title}`

## Salary Rules

- India: 10% deduction
- United States: 12% deduction
- All other countries: no deduction

## Docker

Build the image:

```bash
docker build -t employee-salary-api .
```

Run the API:

```bash
docker run --rm -p 8000:8000 employee-salary-api
```

If you want the SQLite database file to persist on your machine, mount the project directory:

```bash
docker run --rm -p 8000:8000 -v ${PWD}:/app employee-salary-api
```

## TDD Workflow

The repository started with a scaffold commit and then a failing employee creation test. From there, the implementation was expanded in small commits that mostly follow a TDD shape:

- add or tighten tests for a behavior
- implement the smallest change to satisfy the behavior
- refactor or expand assertions once the behavior is stable

Because the history was intentionally expanded to 46 commits, some later commits are coverage-tightening steps rather than strict red-first commits. That is acceptable as long as the overall history still clearly shows behavior-first development.

## Notes On Commit History

- The first two commits were preserved as originally created.
- CRUD, salary, and metrics behavior were then split into many smaller commits to make the evolution easy to inspect.
- The current branch has 46 commits total.

## Implementation Details

- AI was used to help scaffold project structure, draft test cases, refine commit sequencing, and improve documentation.
- Generated code and commit slicing were reviewed manually and adjusted to match the problem statement.
- The final application behavior was verified through the pytest suite.
