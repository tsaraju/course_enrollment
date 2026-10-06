Course Enrollment API

Build a small FastAPI application where students can enroll in courses.

Create APIs to

POST /courses

GET /courses

POST /enroll

GET /students/{student_id}/courses

DELETE /enroll/{enrollment_id}

Prevent a student from enrolling in the same course twice. Return meaningful errors such as 404 when a student/course doesn't exist.

Sample Output:
PS F:\Euron\GitHub\api\course_enrollment> uv run uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['F:\\Euron\\GitHub\\api\\course_enrollment']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [4440] using WatchFiles
INFO:     Started server process [10556]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:59444 - "POST /students HTTP/1.1" 201 Created
INFO:     127.0.0.1:60524 - "POST /students HTTP/1.1" 201 Created
INFO:     127.0.0.1:58493 - "POST /students HTTP/1.1" 201 Created
INFO:     127.0.0.1:52013 - "POST /courses HTTP/1.1" 201 Created
INFO:     127.0.0.1:50203 - "POST /courses HTTP/1.1" 201 Created
INFO:     127.0.0.1:50390 - "POST /courses HTTP/1.1" 201 Created
INFO:     127.0.0.1:56668 - "POST /courses HTTP/1.1" 201 Created
INFO:     127.0.0.1:49467 - "GET /courses HTTP/1.1" 200 OK
INFO:     127.0.0.1:59012 - "POST /enrollments HTTP/1.1" 201 Created
INFO:     127.0.0.1:52430 - "POST /enrollments HTTP/1.1" 201 Created
INFO:     127.0.0.1:62071 - "POST /enrollments HTTP/1.1" 201 Created
INFO:     127.0.0.1:63542 - "GET /enrollments HTTP/1.1" 200 OK
INFO:     127.0.0.1:49321 - "GET /courses/3/students HTTP/1.1" 200 OK
INFO:     127.0.0.1:60306 - "GET /courses/2/students HTTP/1.1" 200 OK
INFO:     127.0.0.1:51913 - "GET /courses/1/students HTTP/1.1" 200 OK
INFO:     127.0.0.1:52942 - "GET /courses/4/students HTTP/1.1" 200 OK
INFO:     127.0.0.1:55746 - "GET /students/3/courses HTTP/1.1" 200 OK
INFO:     127.0.0.1:61485 - "GET /students/1/courses HTTP/1.1" 200 OK
INFO:     127.0.0.1:58366 - "GET /students/2/courses HTTP/1.1" 200 OK
INFO:     127.0.0.1:65029 - "POST /enrollments HTTP/1.1" 409 Conflict
INFO:     127.0.0.1:63567 - "POST /students HTTP/1.1" 201 Created
INFO:     127.0.0.1:55528 - "DELETE /enrollments/2 HTTP/1.1" 204 No Content
INFO:     127.0.0.1:57115 - "DELETE /enrollments/1 HTTP/1.1" 204 No Content
INFO:     127.0.0.1:50107 - "GET /courses HTTP/1.1" 200 OK
INFO:     127.0.0.1:65153 - "GET /enrollments HTTP/1.1" 200 OK
INFO:     127.0.0.1:61849 - "GET /enrollments HTTP/1.1" 200 OK
INFO:     127.0.0.1:58642 - "DELETE /enrollments/5 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:57129 - "DELETE /enrollments/1 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:55612 - "DELETE /enrollments/3 HTTP/1.1" 204 No Content
INFO:     127.0.0.1:61568 - "GET /enrollments HTTP/1.1" 200 OK
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [10556]
INFO:     Stopping reloader process [4440]