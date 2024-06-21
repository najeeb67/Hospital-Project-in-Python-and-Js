from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DoctorBase(BaseModel):
    name: str
    specialization: str

class DoctorCreate(DoctorBase):
    id: Optional[int] = None

class DoctorUpdate(DoctorBase):
    pass

class Doctor(DoctorBase):
    id: int

    class Config:
        orm_mode = True

class PatientBase(BaseModel):
    name: str
    age: int
    condition : str
    admit_date: Optional[datetime] = None
    discharge_date: Optional[datetime] = None
    doctor_id: int

class PatientCreate(PatientBase):
    id: Optional[int] = None
    doctor_id: int

class PatientUpdate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

    class Config:
        orm_mode = True
