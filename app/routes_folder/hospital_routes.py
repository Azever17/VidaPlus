from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.hospital import Hospital as HospitalModel
from app.schemas.hospital import HospitalCreate, HospitalOut
from app.dependencies import get_current_user, get_db

router = APIRouter()

@router.get("/", response_model=List[HospitalOut])
def listar_hospitais(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return db.query(HospitalModel).all()

@router.post("/", response_model=HospitalOut)
def criar_hospital(hospital: HospitalCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_hospital = HospitalModel(**hospital.dict())
    db.add(db_hospital)
    db.commit()
    db.refresh(db_hospital)
    return db_hospital