# employee-salary-api

A small FastAPI service demonstrating employee CRUD operations, salary deduction calculation, and salary metrics endpoints backed by SQLite. The project is intentionally built with an incremental TDD workflow and a detailed commit history to show how the implementation evolved.

## Contents

- Description
- Prerequisites
- Usage
- Environment configuration
- Tests explanation
- TDD flow
- API docs
- Docker
- Project setup
- Implementation details

## Description

This project provides a minimal API for managing employees and calculating salary-related information. It includes:

- REST endpoints implemented with FastAPI
- SQLite persistence using SQLAlchemy
- Request and response validation with Pydantic
- Unit-style API tests using pytest
- Salary deduction rules by country
- Salary metrics endpoints for country and job title
- Incremental commit history showing test-first development

Implemented features:

- Employee CRUD endpoints
- Employee list filtering by country and job title
- Salary breakdown endpoint by employee ID
- Salary metrics by country
- Salary metrics by job title
- Case-insensitive country and job-title matching for salary metrics

Salary rules:

- India: 10% deduction
- United States: 12% deduction
- All other countries: no deduction

## Prerequisites

- Python 3.11 or later
- `pip`
- A terminal with access to the project folder
- Docker Desktop, if you want to run the project in a container

## Usage

Install dependencies and run the app locally.

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -e .[dev]
```

Start the application:

```bash
python -m uvicorn app.main:app --reload
```

By default, the API will be available at:

```text
http://127.0.0.1:8000
```

## Environment Configuration

The application uses SQLite by default and does not require a `.env` file for local execution.

Default database:

```text
sqlite:///./employee_salary.db
```

If needed, you can override the database location with an environment variable:

```bash
set DATABASE_URL=sqlite:///./employee_salary.db
```

On PowerShell:

```powershell
$env:DATABASE_URL="sqlite:///./employee_salary.db"
```

## Tests Explanation

The test suite focuses on endpoint behavior and business rules.

Run all tests:

```bash
python -m pytest
```

Run employee tests only:

```bash
python -m pytest tests/test_employees.py
```

Run salary tests only:

```bash
python -m pytest tests/test_salary.py
```

Run metrics tests only:

```bash
python -m pytest tests/test_metrics.py
```

The current test coverage includes:

- Employee creation, listing, fetch, update, and delete
- Employee list filtering by country and job title
- Validation failures for invalid employee input
- Salary deduction calculation for India
- Salary deduction calculation for United States
- Salary fallback behavior for other countries
- Salary metrics by country
- Salary metrics by job title
- Case-insensitive salary metrics lookup by country and job title
- Empty-result cases for metrics endpoints

Tests use an isolated in-memory SQLite database so they remain fast and deterministic.

## TDD Flow

The project was developed using small test-first steps.

Recommended workflow:

1. Write a failing test for the next behavior.
2. Run the relevant test and confirm it fails.
3. Implement the smallest change needed to make it pass.
4. Run the test again and confirm it passes.
5. Refactor where needed while keeping the test suite green.
6. Repeat for the next behavior.

Examples from this project:

- Add a failing employee creation test
- Implement the employee creation endpoint
- Add a failing employee list test
- Implement the employee list endpoint
- Add salary calculation tests for each rule
- Implement the deduction logic
- Add metrics tests
- Implement aggregation endpoints
- Add filtering tests before implementing employee list filters
- Add case-insensitive metrics tests before changing metrics queries

## API Docs

FastAPI provides interactive API documentation out of the box.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

These pages can be used to inspect request/response schemas and try endpoints from the browser.

## Docker

Build the image:

```bash
docker build -t employee-salary-api .
```

Run the container:

```bash
docker run --rm -p 8000:8000 employee-salary-api
```

If you want the SQLite database file to persist on your machine, mount the project directory:

```bash
docker run --rm -p 8000:8000 -v ${PWD}:/app employee-salary-api
```

## Project Setup

Install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -e .[dev]
```

Run the application:

```bash
python -m uvicorn app.main:app --reload
```

Run tests:

```bash
python -m pytest
```

Run a specific test file:

```bash
python -m pytest tests/test_employees.py
```

## API Endpoints

### Employee

- `POST /employees`
- `GET /employees`
- `GET /employees?country=India`
- `GET /employees?job_title=Software Engineer`
- `GET /employees?country=India&job_title=Software Engineer`
- `GET /employees/{employee_id}`
- `PUT /employees/{employee_id}`
- `DELETE /employees/{employee_id}`

### Salary

- `GET /employees/{employee_id}/salary`

### Metrics

- `GET /metrics/salary/country/{country}`
- `GET /metrics/salary/job-title/{job_title}`

Metrics lookups for country and job title are case-insensitive. For example, `India`, `india`, and `INDIA` match the same country value.

## Implementation Details

This project was implemented with AI assistance as part of the assessment workflow. The AI assistance was used intentionally for speed, structure, and review, while the final code, test behavior, and trade-offs were verified manually.

Tools used:

- ChatGPT/Codex-style coding assistant
- Local terminal commands for pytest, git history inspection, and project verification
- FastAPI, SQLAlchemy, Pydantic, pytest, and Docker documentation patterns from standard project usage

How AI was used:

- To scaffold the initial FastAPI project structure, including `app`, `api`, `db`, `schemas`, `services`, and `tests` folders.
- To draft focused pytest cases for employee CRUD, salary calculation rules, and salary metrics edge cases.
- To draft and refine README sections, including setup, testing, Docker, and API usage instructions.

Example prompts used during the workflow:

- "Create a Python FastAPI project structure for an employee salary API using SQLite and pytest."
- "Write failing pytest tests for employee creation, list, fetch, update, and delete endpoints."
- "Add tests for salary calculation rules for India, United States, and all other countries."
- "Rewrite the README in a clear interview-assessment style with setup, tests, TDD flow, and Docker instructions."

Rationale for using AI:

- To move quickly from the problem statement to a working project skeleton.
- To generate multiple test scenarios faster while keeping them deterministic and readable.
- To improve documentation clarity and ensure the README covers how to run, test, and inspect the project.

Manual review and verification:

- Tests were run locally with `python -m pytest`.
- Endpoint behavior was validated through API-level pytest tests rather than only service-level tests.
- The final implementation was checked against the original requirements: employee CRUD, SQLite persistence, salary calculation by country, salary metrics by country, and salary metrics by job title.

Key implementation decisions:

- SQLite was chosen because it matches the assessment requirement and keeps setup lightweight.
- SQLAlchemy is used for persistence and query handling.
- FastAPI was chosen for clear request validation, simple routing, and built-in API documentation.
- Tests are written against the API surface to validate request/response behavior end to end.
- The commit history was intentionally kept granular to make the development flow easy to review.
