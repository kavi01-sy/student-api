# Student API

A small REST API for an NGO skilling programme: lists students, adds students,
and summarises attendance. Training project, dummy data only.

## Stack
- Python 3.14, FastAPI, uvicorn, Pydantic
- SQLite database: `skilling_programme.db`
- Frontend: `index.html` (plain HTML + JavaScript fetch), served by FastAPI at `/page`
- Deployed on Render: https://student-api-1hrm.onrender.com

## Files
- `main.py`: all API routes
- `index.html`: page that lists students
- `skilling_programme.db`: SQLite database (dummy data)
- `requirements.txt`: Python packages

## Database (exact names; spelling matters)
- Tables: `Batch`, `Student`, `Session`, `Attendance`, `Placement`
- `Student` columns: `Student_ID`, `Batch_ID`, `Student_Name`, `Email`, `Phone`,
  `Date_of_Birth`, `Gender`, `Enrolment_Date` (one L), `Status`
- `Attendance` columns: `Attendance_ID`, `Student_ID`, `Session_ID`, `Status`
- Attendance `Status` has mixed case (`Present` / `present`): always compare with `LOWER()`

## Endpoints
- `GET /`: health message using `APP_NAME`
- `GET /students`: list all students
- `POST /students`: add a student (validated by the `NewStudent` Pydantic model)
- `GET /attendance/summary`: per-student attendance (LEFT JOIN, so students with no attendance appear)
- `GET /page`: serves `index.html`

## Commands
- Run locally (PowerShell):
  `$env:APP_NAME="Student API"` then `uvicorn main:app --reload`
- Render start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

## Rules
- Environment variable `APP_NAME` is required; the name must be exactly `APP_NAME`.
- Never put secrets (keys, passwords, tokens) in code. Use environment variables.
- Always use `?` placeholders in SQL. Never build SQL by joining strings.
- Use `conn.commit()` after INSERT/UPDATE/DELETE, and always `conn.close()`.
- Test data uses `@example.com` emails only. No real personal data.
- `index.html` must call the API with relative URLs (`/students`), not `127.0.0.1`.
- Tag AI-assisted commits with "(AI-assisted)".