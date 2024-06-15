from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    StudentID = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    DOB = Column(Date, nullable=False)
    Email = Column(String, unique=True, nullable=False)

    enrollments = relationship('Enrollment', back_populates='student')

class Course(Base):
    __tablename__ = 'courses'
    CourseID = Column(Integer, primary_key=True, autoincrement=True)
    CourseName = Column(String, nullable=False)
    Credits = Column(Integer, nullable=False)

    enrollments = relationship('Enrollment', back_populates='course')

class Enrollment(Base):
    __tablename__ = 'enrollments'
    EnrollmentID = Column(Integer, primary_key=True, autoincrement=True)
    CourseID = Column(Integer, ForeignKey('courses.CourseID'), nullable=False)
    StudentID = Column(Integer, ForeignKey('students.StudentID'), nullable=False)
    EnrollmentDate = Column(Date, nullable=False)

    student = relationship('Student', back_populates='enrollments')
    course = relationship('Course', back_populates='enrollments')
    grades = relationship('Grade', back_populates='enrollment')

class Grade(Base):
    __tablename__ = 'grades'
    GradeID = Column(Integer, primary_key=True, autoincrement=True)
    EnrollmentID = Column(Integer, ForeignKey('enrollments.EnrollmentID'), nullable=False)
    Grade = Column(String, nullable=False)

    enrollment = relationship('Enrollment', back_populates='grades')
