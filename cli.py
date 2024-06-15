from datetime import datetime
from database import init_db, SessionLocal
from models import Student, Course, Enrollment, Grade

def input_date(prompt):
    while True:
        try:
            return datetime.strptime(input(prompt), "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def add_student():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    dob = input_date("Enter date of birth (YYYY-MM-DD): ")
    email = input("Enter email: ")
    session = SessionLocal()
    new_student = Student(FirstName=first_name, LastName=last_name, DOB=dob, Email=email)
    session.add(new_student)
    session.commit()
    session.close()
    print("Student added successfully.")

def list_students():
    session = SessionLocal()
    students = session.query(Student).all()
    session.close()
    for student in students:
        print(f'{student.StudentID}: {student.FirstName} {student.LastName}, {student.Email}')

def find_student():
    email = input("Enter email to find: ")
    session = SessionLocal()
    student = session.query(Student).filter_by(Email=email).first()
    session.close()
    if student:
        print(f'{student.StudentID}: {student.FirstName} {student.LastName}, {student.Email}')
    else:
        print("Student not found.")

def delete_student():
    student_id = input_int("Enter student ID to delete: ")
    session = SessionLocal()
    student = session.query(Student).filter_by(StudentID=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print("Student deleted successfully.")
    else:
        print("Student not found.")
    session.close()

def add_course():
    course_name = input("Enter course name: ")
    credits = input_int("Enter number of credits: ")
    session = SessionLocal()
    new_course = Course(CourseName=course_name, Credits=credits)
    session.add(new_course)
    session.commit()
    session.close()
    print("Course added successfully.")

def list_courses():
    session = SessionLocal()
    courses = session.query(Course).all()
    session.close()
    for course in courses:
        print(f'{course.CourseID}: {course.CourseName}, Credits: {course.Credits}')

def find_course():
    course_name = input("Enter course name to find: ")
    session = SessionLocal()
    course = session.query(Course).filter_by(CourseName=course_name).first()
    session.close()
    if course:
        print(f'{course.CourseID}: {course.CourseName}, Credits: {course.Credits}')
    else:
        print("Course not found.")

def delete_course():
    course_id = input_int("Enter course ID to delete: ")
    session = SessionLocal()
    course = session.query(Course).filter_by(CourseID=course_id).first()
    if course:
        session.delete(course)
        session.commit()
        print("Course deleted successfully.")
    else:
        print("Course not found.")
    session.close()

def enroll_student():
    student_id = input_int("Enter student ID: ")
    course_id = input_int("Enter course ID: ")
    enrollment_date = input_date("Enter enrollment date (YYYY-MM-DD): ")
    session = SessionLocal()
    new_enrollment = Enrollment(StudentID=student_id, CourseID=course_id, EnrollmentDate=enrollment_date)
    session.add(new_enrollment)
    session.commit()
    session.close()
    print("Student enrolled successfully.")

def list_enrollments():
    session = SessionLocal()
    enrollments = session.query(Enrollment).all()
    session.close()
    for enrollment in enrollments:
        student = enrollment.student
        course = enrollment.course
        print(f'EnrollmentID: {enrollment.EnrollmentID}, Student: {student.FirstName} {student.LastName}, Course: {course.CourseName}, Date: {enrollment.EnrollmentDate}')

def run_cli():
    init_db()
    while True:
        print("\nStudent Information System")
        print("1. Add Student")
        print("2. List Students")
        print("3. Find Student")
        print("4. Delete Student")
        print("5. Add Course")
        print("6. List Courses")
        print("7. Find Course")
        print("8. Delete Course")
        print("9. Enroll Student")
        print("10. List Enrollments")
        print("11. Exit")
        
        choice = input_int("Choose an option: ")
        
        if choice == 1:
            add_student()
        elif choice == 2:
            list_students()
        elif choice == 3:
            find_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            add_course()
        elif choice == 6:
            list_courses()
        elif choice == 7:
            find_course()
        elif choice == 8:
            delete_course()
        elif choice == 9:
            enroll_student()
        elif choice == 10:
            list_enrollments()
        elif choice == 11:
            break
        else:
            print("Invalid choice. Please try again.")
