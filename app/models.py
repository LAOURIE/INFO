from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    StudentID = Column(Integer, primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)
    DOB = Column(Date)
    Email = Column(String)

    enrollments = relationship('Enrollment', back_populates='student')

    class Enrollments(Base):
        __tablename__ = 'enrollments'
        EnrollmentID = Column(Integer, primary_key=True)
        CourseID = Column(Integer, ForeignKey('courses.CourseID'))
        StudentID = Column(Integer, ForeignKey('students.StudentID'))
        EnrollmentDate = Column(Date)

        student = relationship('Student', back_populates='enrollments')
        course = relationship('Course', back_populates='enrollments')
        grades = relationship('Grade', back_populates='enrolment')

    class Grade(Base):
        __tablename__ = 'grades'
        GradeID = Column(Integer, primary_key=True)
        EnrollmentID = Column(Integer, ForeignKey('enrollments.EnrollmentID'))
        Grade = Column(String)

        enrolment = relationship('Enrollment', back_populates='grades')

