from sqlalchemy.orm import Session
from model import *
from schemas import *
from model import Doctor , Patient , Appointment
from typing import List

def get_doctor(db: Session, doctor_id: int):
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()

def get_doctors(db: Session, skip: int = 0, limit: int = 10) -> List[Doctor]:
    return db.query(Doctor).offset(skip).limit(limit).all()

def create_doctor(db: Session, doctor: DoctorCreate):
    db_doctor = Doctor(
        name=doctor.name,
        specialization=doctor.specialization,
        department=doctor.department  
    )
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


def update_doctor(db: Session, doctor_id: int, doctor: DoctorUpdate):
    db_doctor = get_doctor(db, doctor_id)
    if db_doctor:
        for key, value in doctor.dict().items():
            setattr(db_doctor, key, value)
        db.commit()
        db.refresh(db_doctor)
    return db_doctor

def delete_doctor(db: Session, doctor_id: int):
    db_doctor = get_doctor(db, doctor_id)
    if db_doctor:
        db.delete(db_doctor)
        db.commit()
    return db_doctor


def get_patient(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()

def get_patients(db: Session, skip: int = 0, limit: int = 10) -> List[Patient]:
    return db.query(Patient).offset(skip).limit(limit).all()

def create_patient(db: Session, patient: PatientCreate):
    db_patient = Patient(
        name=patient.name,
        age=patient.age,
        condition=patient.condition,
        doctor_id=1 
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


def update_patient(db: Session, patient_id: int, patient: PatientUpdate):
    db_patient = get_patient(db, patient_id)
    if db_patient:
        for key, value in patient.dict().items():
            setattr(db_patient, key, value)
        db.commit()
        db.refresh(db_patient)
    return db_patient

def delete_patient(db: Session, patient_id: int):
    db_patient = get_patient(db, patient_id)
    if db_patient:
        db.delete(db_patient)
        db.commit()
    return db_patient

def get_appointment(db: Session, appointment_id: int):
    return db.query(Appointment).filter(Appointment.id == appointment_id).first()

def get_appointments(db: Session, skip: int = 0, limit: int = 10) -> List[Appointment]:
    return db.query(Appointment).offset(skip).limit(limit).all()

def create_appointment(db: Session, appointment: AppointmentCreate):
    db_appointment = Appointment(
        doctor_id=appointment.doctor_id,
        patient_id=appointment.patient_id,
        appointment_time=appointment.appointment_time,
        charges=appointment.charges
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def update_appointment(db: Session, appointment_id: int, appointment: AppointmentUpdate):
    db_appointment = get_appointment(db, appointment_id)
    if db_appointment:
        for key, value in appointment.dict().items():
            setattr(db_appointment, key, value)
        db.commit()
        db.refresh(db_appointment)
    return db_appointment

def delete_appointment(db: Session, appointment_id: int):
    db_appointment = get_appointment(db, appointment_id)
    if db_appointment:
        db.delete(db_appointment)
        db.commit()
    return db_appointment
    
    
def get_departments(db: Session):
    return db.query(Doctor.department).distinct().all()

def get_doctors_by_department(db: Session, department: str):
    return db.query(Doctor).filter(Doctor.department == department).all()
