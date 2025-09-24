from pydantic import BaseModel
from datetime import date

class InstituteSchema(BaseModel):
    name: str

class CourseSchema(BaseModel):
    title: str
    institute_id: int

class BatchSchema(BaseModel):
    course_id: int
    batch_name: str
    start_date: date
    end_date: date

class StudentSchema(BaseModel):
    name: str
    email: str
    batch_id: int

class FeeSchema(BaseModel):
    student_id: int
    total_amount: float
    pending_amount: float

class InstallmentSchema(BaseModel):
    amount_paid: float
    payment_date: date