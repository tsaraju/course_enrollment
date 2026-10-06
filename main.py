from itertools import count

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Course Enrollment API")


# ---------- Schemas ----------

class StudentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: str = Field(min_length=3, max_length=100)


class Student(StudentCreate):
    id: int


class CourseCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = ""


class Course(CourseCreate):
    id: int


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int


class Enrollment(EnrollmentCreate):
    id: int


# ---------- In-memory storage ----------
students: dict[int, Student] = {}
courses: dict[int, Course] = {}
enrollments: dict[int, Enrollment] = {}

student_ids = count(1)
course_ids = count(1)
enrollment_ids = count(1)

# Seed data so enrollment can be tested immediately
for name, email in [("Asha", "asha@example.com"), ("Ravi", "ravi@example.com")]:
    sid = next(student_ids)
    students[sid] = Student(id=sid, name=name, email=email)


# ---------- Helpers ----------
def get_student_or_404(student_id: int) -> Student:
    student = students.get(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail=f"Student {student_id} not found")
    return student


def get_course_or_404(course_id: int) -> Course:
    course = courses.get(course_id)
    if course is None:
        raise HTTPException(status_code=404, detail=f"Course {course_id} not found")
    return course


# ---------- Students (helper endpoint) ----------
@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(payload: StudentCreate):
    student = Student(id=next(student_ids), **payload.model_dump())
    students[student.id] = student
    return student


# ---------- Courses ----------
@app.post("/courses", response_model=Course, status_code=status.HTTP_201_CREATED)
def create_course(payload: CourseCreate):
    course = Course(id=next(course_ids), **payload.model_dump())
    courses[course.id] = course
    return course


@app.get("/courses", response_model=list[Course])
def list_courses():
    return list(courses.values())

# ---------- Enrollments ----------
@app.post("/enrollments", response_model=Enrollment, status_code=status.HTTP_201_CREATED)
def enroll_student(payload: EnrollmentCreate):
    # Validate both sides exist (reuses your helpers)
    get_student_or_404(payload.student_id)
    get_course_or_404(payload.course_id)

    # Prevent duplicate enrollment
    for e in enrollments.values():
        if e.student_id == payload.student_id and e.course_id == payload.course_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Student already enrolled in this course",
            )

    enrollment = Enrollment(id=next(enrollment_ids), **payload.model_dump())
    enrollments[enrollment.id] = enrollment
    return enrollment


@app.get("/enrollments", response_model=list[Enrollment])
def list_enrollments():
    return list(enrollments.values())


@app.get("/courses/{course_id}/students", response_model=list[Student])
def list_course_students(course_id: int):
    get_course_or_404(course_id)
    return [
        students[e.student_id]
        for e in enrollments.values()
        if e.course_id == course_id
    ]


@app.get("/students/{student_id}/courses", response_model=list[Course])
def list_student_courses(student_id: int):
    get_student_or_404(student_id)
    return [
        courses[e.course_id]
        for e in enrollments.values()
        if e.student_id == student_id
    ]


@app.delete("/enrollments/{enrollment_id}", status_code=status.HTTP_204_NO_CONTENT)
def unenroll(enrollment_id: int):
    if enrollment_id not in enrollments:
        raise HTTPException(status_code=404, detail=f"Enrollment {enrollment_id} not found")
    del enrollments[enrollment_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)