from contextlib import asynccontextmanager
from typing import List

from fastapi import FastAPI, Depends, HTTPException, Query
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from database.db import init_db, get_session
from backend.models import (
    Student, StudentCreate, StudentRead,
    Course, CourseCreate, CourseRead,
    StudentCourseLink
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create tables
    await init_db()
    yield
    # Shutdown: Clean up if needed

app = FastAPI(lifespan=lifespan, title="Luxury Academy API")

# --- Student Ends ---

@app.post("/students/", response_model=StudentRead)
async def create_student(
    student: StudentCreate, 
    session: AsyncSession = Depends(get_session)
):
    db_student = Student.model_validate(student)
    session.add(db_student)
    await session.commit()
    await session.refresh(db_student)
    return db_student

@app.get("/students/", response_model=List[StudentRead])
async def read_students(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    session: AsyncSession = Depends(get_session)
):
    result = await session.exec(select(Student).offset(offset).limit(limit))
    students = result.all()
    return students

@app.get("/students/{student_id}", response_model=StudentRead)
async def read_student(
    student_id: int, 
    session: AsyncSession = Depends(get_session)
):
    student = await session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# --- Course Ends ---

@app.post("/courses/", response_model=CourseRead)
async def create_course(
    course: CourseCreate, 
    session: AsyncSession = Depends(get_session)
):
    db_course = Course.model_validate(course)
    session.add(db_course)
    await session.commit()
    await session.refresh(db_course)
    return db_course

@app.get("/courses/", response_model=List[CourseRead])
async def read_courses(
    offset: int = 0,
    limit: int = 100,
    session: AsyncSession = Depends(get_session)
):
    result = await session.exec(select(Course).offset(offset).limit(limit))
    return result.all()

# --- Enrollment ---

@app.post("/students/{student_id}/courses/{course_id}")
async def enroll_student(
    student_id: int,
    course_id: int,
    session: AsyncSession = Depends(get_session)
):
    student = await session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    course = await session.get(Course, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
        
    # Check if already enrolled (basic check)
    # real impl might check existing links
    
    student.courses.append(course)
    session.add(student)
    await session.commit()
    return {"message": "Enrolled successfully", "student": student.name, "course": course.name}
