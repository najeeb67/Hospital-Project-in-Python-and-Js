from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DoctorBase(BaseModel):
    name: str
    specialization: str
    time_in: Optional[datetime] = None
    time_out: Optional[datetime] = None

class DoctorCreate(DoctorBase):
    pass

class DoctorUpdate(DoctorBase):
    pass

class Doctor(DoctorBase):
    id: int

    class Config:
        from_attributes = True

class PatientBase(BaseModel):
    name: str
    age: int
    admit_date: Optional[datetime] = None
    discharge_date: Optional[datetime] = None
    doctor_id: int

class PatientCreate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

    class Config:
        from_attributes = True
