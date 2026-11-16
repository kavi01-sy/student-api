from fastapi import FastAPI
from pydantic import BaseModel

import sqlite3
class NewStudent(BaseModel):
    Batch_ID: int
    Student_Name: str
    Email: str
    Phone: str
    Date_of_Birth: str
    Gender: str
    Enrolment_Date: str
    Status: str
    


app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {"Message": "Hurray! API is Working!"}

@app.get('/hello')
def greet():
    return {"Greeting":"Helloo Kavii"}

import sqlite3
@app.get("/students")
def get_students():
    conn = sqlite3.connect("skilling_programme.db")
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM student").fetchall()
    students = [dict(row) for row in rows] 
    conn.close()
    return(students)

@app.post('/students')
def add_student(student: NewStudent):
    conn =sqlite3.connect("skilling_programme.db")
    conn.execute(
        "INSERT INTO Student (Batch_ID, Student_Name, Email, Phone, Date_of_Birth, Gender, Enrolment_Date, Status) VALUES (?,?,?,?,?,?,?,?)",
        (student.Batch_ID, student.Student_Name, student.Email, student.Phone, student.Date_of_Birth, student.Gender, student.Enrolment_Date, student.Status)
        )
    conn.commit()
    conn.close()
    return {"Message": "Student Added"}

@app.get("/attendance/summary")
def attendance_summary():
    conn = sqlite3.connect("skilling_programme.db")
    conn.row_factory = sqlite3.Row
    query = """
        SELECT
            Student.Student_ID,
            Student.Student_Name,
            COUNT(*) AS Total_Sessions,
            SUM(CASE WHEN LOWER(Attendance.Status) = 'present' THEN 1 ELSE 0 END) AS Present,
            ROUND(100.0 * SUM(CASE WHEN LOWER(Attendance.Status) = 'present' THEN 1 ELSE 0 END) / COUNT(*), 1) AS Attendance_Percent
        FROM Attendance
        JOIN Student ON Attendance.Student_ID = Student.Student_ID
        GROUP BY Student.Student_ID, Student.Student_Name
        ORDER BY Attendance_Percent
    """
    rows = conn.execute(query).fetchall()
    summary = [dict(row) for row in rows]
    conn.close()
    return summary

    
    




