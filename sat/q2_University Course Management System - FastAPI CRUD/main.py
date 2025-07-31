from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List, Optional

app = FastAPI()

# ------------------- Models -------------------

class Student(BaseModel):
    id: int
    name: str
    email: EmailStr
    major: str
    year: int
    gpa: float = 0.0

class Course(BaseModel):
    id: int
    name: str
    code: str
    credits: int
    professor_id: int
    max_capacity: int

class Professor(BaseModel):
    id: int
    name: str
    email: EmailStr
    department: str
    hire_date: date

class Enrollment(BaseModel):
    student_id: int
    course_id: int
    enrollment_date: date
    grade: Optional[float] = None

# ------------------- In-Memory "Database" -------------------

students_db = {}
courses_db = {}
professors_db = {}
enrollments_db = []

# ------------------- Students -------------------

@app.post("/students")
def create_student(student: Student):
    if student.id in students_db:
        raise HTTPException(status_code=400, detail="Student already exists")
    students_db[student.id] = student
    return student

@app.get("/students")
def get_all_students():
    return list(students_db.values())

@app.get("/students/{id}")
def get_student(id: int):
    student = students_db.get(id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{id}")
def update_student(id: int, student: Student):
    if id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    students_db[id] = student
    return student

@app.delete("/students/{id}")
def delete_student(id: int):
    if id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    del students_db[id]
    return {"message": "Student deleted"}

@app.get("/students/{id}/courses")
def get_student_courses(id: int):
    if id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    enrolled_courses = [
        course for course in enrollments_db if course.student_id == id
    ]
    return [courses_db[en.course_id] for en in enrolled_courses if en.course_id in courses_db]

# ------------------- Courses -------------------

@app.post("/courses")
def create_course(course: Course):
    if course.id in courses_db:
        raise HTTPException(status_code=400, detail="Course already exists")
    courses_db[course.id] = course
    return course

@app.get("/courses")
def get_all_courses():
    return list(courses_db.values())

@app.get("/courses/{id}")
def get_course(id: int):
    course = courses_db.get(id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.put("/courses/{id}")
def update_course(id: int, course: Course):
    if id not in courses_db:
        raise HTTPException(status_code=404, detail="Course not found")
    courses_db[id] = course
    return course

@app.delete("/courses/{id}")
def delete_course(id: int):
    if id not in courses_db:
        raise HTTPException(status_code=404, detail="Course not found")
    del courses_db[id]
    return {"message": "Course deleted"}

@app.get("/courses/{id}/students")
def get_course_students(id: int):
    if id not in courses_db:
        raise HTTPException(status_code=404, detail="Course not found")
    enrolled = [e for e in enrollments_db if e.course_id == id]
    return [students_db[e.student_id] for e in enrolled if e.student_id in students_db]

# ------------------- Professors -------------------

@app.post("/professors")
def create_professor(prof: Professor):
    if prof.id in professors_db:
        raise HTTPException(status_code=400, detail="Professor already exists")
    professors_db[prof.id] = prof
    return prof

@app.get("/professors")
def get_all_professors():
    return list(professors_db.values())

@app.get("/professors/{id}")
def get_professor(id: int):
    prof = professors_db.get(id)
    if not prof:
        raise HTTPException(status_code=404, detail="Professor not found")
    return prof

@app.put("/professors/{id}")
def update_professor(id: int, prof: Professor):
    if id not in professors_db:
        raise HTTPException(status_code=404, detail="Professor not found")
    professors_db[id] = prof
    return prof

@app.delete("/professors/{id}")
def delete_professor(id: int):
    if id not in professors_db:
        raise HTTPException(status_code=404, detail="Professor not found")
    del professors_db[id]
    return {"message": "Professor deleted"}

@app.get("/professors/{id}/courses")
def get_professor_courses(id: int):
    if id not in professors_db:
        raise HTTPException(status_code=404, detail="Professor not found")
    return [c for c in courses_db.values() if c.professor_id == id]

# ------------------- Enrollments -------------------

@app.post("/enrollments")
def enroll_student(enroll: Enrollment):
    if enroll.student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    if enroll.course_id not in courses_db:
        raise HTTPException(status_code=404, detail="Course not found")

    current_enrolled = sum(1 for e in enrollments_db if e.course_id == enroll.course_id)
    course = courses_db[enroll.course_id]

    if current_enrolled >= course.max_capacity:
        raise HTTPException(status_code=400, detail="Course is full")

    # Check duplicate enrollment
    for e in enrollments_db:
        if e.student_id == enroll.student_id and e.course_id == enroll.course_id:
            raise HTTPException(status_code=400, detail="Already enrolled")

    enrollments_db.append(enroll)
    return enroll

@app.get("/enrollments")
def get_all_enrollments():
    return enrollments_db

@app.put("/enrollments/{student_id}/{course_id}")
def update_grade(student_id: int, course_id: int, grade: float):
    for e in enrollments_db:
        if e.student_id == student_id and e.course_id == course_id:
            e.grade = grade
            recalculate_gpa(student_id)
            return e
    raise HTTPException(status_code=404, detail="Enrollment not found")

@app.delete("/enrollments/{student_id}/{course_id}")
def drop_course(student_id: int, course_id: int):
    global enrollments_db
    enrollments_db = [
        e for e in enrollments_db
        if not (e.student_id == student_id and e.course_id == course_id)
    ]
    recalculate_gpa(student_id)
    return {"message": "Course dropped"}

# ------------------- GPA Calculation -------------------

def recalculate_gpa(student_id: int):
    grades = [e.grade for e in enrollments_db if e.student_id == student_id and e.grade is not None]
    if grades:
        gpa = sum(grades) / len(grades)
        students_db[student_id].gpa = round(gpa, 2)
    else:
        students_db[student_id].gpa = 0.0
