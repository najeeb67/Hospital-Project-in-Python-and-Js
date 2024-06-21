from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
import crud
import schemas
from schemas import Doctor, DoctorCreate, DoctorUpdate, Patient, PatientCreate, PatientUpdate
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:8080"
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
