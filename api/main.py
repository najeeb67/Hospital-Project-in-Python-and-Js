from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
import crud
import schemas
from schemas import *
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

init_db()

@app.post("/doctors/", response_model=Doctor)
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    return crud.create_doctor(db=db, doctor=doctor)

@app.get("/doctors/{doctor_id}", response_model=Doctor)
def read_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_doctor = crud.get_doctor(db, doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return db_doctor

@app.get("/doctors/", response_model=List[schemas.Doctor])
def read_doctors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    doctors = crud.get_doctors(db, skip=skip, limit=limit)
    return doctors

@app.put("/doctors/{doctor_id}", response_model=Doctor)
def update_doctor(doctor_id: int, doctor: DoctorUpdate, db: Session = Depends(get_db)):
    db_doctor = crud.update_doctor(db, doctor_id, doctor)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return db_doctor

@app.delete("/doctors/{doctor_id}", response_model=Doctor)
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_doctor = crud.delete_doctor(db, doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return db_doctor

@app.post("/patients/", response_model=Patient)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    print(patient.dict())
    return crud.create_patient(db=db, patient=patient)

@app.get("/patients/{patient_id}", response_model=Patient)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = crud.get_patient(db, patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@app.get("/patients/", response_model=List[Patient])
def read_patients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    patients = crud.get_patients(db, skip=skip, limit=limit)
    return patients

@app.put("/patients/{patient_id}", response_model=Patient)
def update_patient(patient_id: int, patient: PatientUpdate, db: Session = Depends(get_db)):
    db_patient = crud.update_patient(db, patient_id, patient)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@app.delete("/patients/{patient_id}", response_model=Patient)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = crud.delete_patient(db, patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@app.post("/appointments/", response_model=Appointment)
def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    return crud.create_appointment(db=db, appointment=appointment)

@app.get("/appointments/{appointment_id}", response_model=Appointment)
def read_appointment(appointment_id: int, db: Session = Depends(get_db)):
    db_appointment = crud.get_appointment(db, appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment

@app.get("/appointments/", response_model=List[Appointment])
def read_appointments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    appointments = crud.get_appointments(db, skip=skip, limit=limit)
    return appointments

@app.put("/appointments/{appointment_id}", response_model=Appointment)
def update_appointment(appointment_id: int, appointment: AppointmentUpdate, db: Session = Depends(get_db)):
    db_appointment = crud.update_appointment(db, appointment_id, appointment)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment

@app.delete("/appointments/{appointment_id}", response_model=Appointment)
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    db_appointment = crud.delete_appointment(db, appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment


@app.get("/departments/", response_model=List[str])
def read_departments(db: Session = Depends(get_db)):
    departments = crud.get_departments(db)
    return [d[0] for d in departments]

@app.get("/departments/{department}/doctors", response_model=List[Doctor])
def read_doctors_by_department(department: str, db: Session = Depends(get_db)):
    doctors = crud.get_doctors_by_department(db, department)
    return doctors
