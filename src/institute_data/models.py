from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from src.utils.db import Base


class Institute(Base):
    __tablename__ = "institutes"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    courses = relationship("Course", back_populates="institute", passive_deletes="all, delete-orphan")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    institute_id = Column(Integer, ForeignKey("institutes.id", ondelete="CASCADE"))

    institute = relationship("Institute", back_populates="courses", passive_deletes=True)
    batches = relationship("Batch", back_populates="course", passive_deletes="all, delete-orphan")


class Batch(Base):
    __tablename__ = "batches"

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id",ondelete="CASCADE"))
    batch_name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)

    course = relationship("Course", back_populates="batches", passive_deletes=True)
    students = relationship("Student", back_populates="batch",passive_deletes="all, delete-orphan")


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    batch_id = Column(Integer, ForeignKey("batches.id",ondelete="CASCADE"))

    batch = relationship("Batch", back_populates="students", passive_deletes=True)
    fees = relationship("Fee", back_populates="student", passive_deletes="all,delete-orphan")


class Fee(Base):
    __tablename__ = "fees"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id",ondelete="CASCADE"))
    total_amount = Column(Float)
    pending_amount = Column(Float)

    student = relationship("Student", back_populates="fees", passive_deletes=True)
    installments = relationship("Installment", back_populates="fee", passive_deletes="all, delete-orphan")


class Installment(Base):
    __tablename__ = "installments"

    id = Column(Integer, primary_key=True)
    fee_id = Column(Integer, ForeignKey("fees.id", ondelete="CASCADE"))
    amount_paid = Column(Float)
    payment_date = Column(Date)

    fee = relationship("Fee", back_populates="installments", passive_deletes=True)
