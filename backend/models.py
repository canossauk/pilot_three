from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

# Link table for Many-to-Many relationship between Student and Course
class StudentCourseLink(SQLModel, table=True):
    student_id: Optional[int] = Field(
        default=None, foreign_key="student.id", primary_key=True
    )
    course_id: Optional[int] = Field(
        default=None, foreign_key="course.id", primary_key=True
    )

class StudentBase(SQLModel):
    name: str = Field(index=True)
    email: str = Field(unique=True, index=True)
    age: Optional[int] = None
    major: Optional[str] = None

class Student(StudentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # Relationship
    courses: List["Course"] = Relationship(back_populates="students", link_model=StudentCourseLink)

class StudentCreate(StudentBase):
    pass

class StudentRead(StudentBase):
    id: int

class CourseBase(SQLModel):
    name: str
    description: Optional[str] = None
    credits: int = 3

class Course(CourseBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # Relationship
    students: List[Student] = Relationship(back_populates="courses", link_model=StudentCourseLink)

class CourseCreate(CourseBase):
    pass

class CourseRead(CourseBase):
    id: int
