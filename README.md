# Student API

A small REST API built with FastAPI and SQLite for an NGO skilling programme (dummy data).

## Endpoints

| Method | Path | What it does |
|---|---|---|
| GET | /students | ... |
| POST | /students | ... |
| GET | /attendance/summary | ... |

## How to run

1. Create and activate a virtual environment
2. pip install -r requirements.txt
3. uvicorn main:app --reload
4. Open http://127.0.0.1:8000/docs

## What I learned

## What I learned

- **How an API works:** a client (browser, Postman or Zoho Creator) sends a request to a route, FastAPI runs the matching function, and the function talks to the database and returns JSON.
- **Routes and methods:** the same path (`/students`) can do different things depending on the method. GET reads data, POST adds data.
- **Talking to SQLite from Python:** connect → execute → fetchall → close, and `commit()` after any change, otherwise nothing is saved.
- **Rows to JSON:** `row_factory = sqlite3.Row` keeps the column names, and `dict(row)` turns each row into a dictionary that FastAPI can send as JSON.
- **Validating input with Pydantic:** the `NewStudent` model rejects bad or missing data with a 422 error before it reaches the database.
- **Safe SQL:** values from users go into `?` placeholders, never straight into the SQL text, to prevent SQL injection.
- **Messy data:** the attendance data had both `Present` and `present`, so I used `LOWER()` to count them correctly. The code ran without errors either way, but the answer was wrong without it.
- **Reading errors:** in a long traceback, look at the last line (what went wrong) and the line with my own file name (where). I fixed a spelling mismatch (`Enrollment_Date` vs `Enrolment_Date`) and a missing comma (`'str' object is not callable`) this way.
- **Testing in Postman:** saved a collection with a request for each endpoint, and saw a 422 when the request body was missing.
## Notes

AI-assisted: built step by step with guidance from Claude; all code written and reviewed by me.