from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.resident import Resident
from app.schemas.resident import ResidentCreate, ResidentResponse


router = APIRouter(
    prefix="/residents",
    tags=["Residents"],
)


@router.post("", response_model=ResidentResponse, status_code=201)
def create_resident(
    resident: ResidentCreate,
    db: Session = Depends(get_db),
):
    new_resident = Resident(
        full_name=resident.full_name,
        date_of_birth=resident.date_of_birth,
        room_number=resident.room_number,
        emergency_contact=resident.emergency_contact,
    )

    db.add(new_resident)
    db.commit()
    db.refresh(new_resident)

    return new_resident


@router.get("", response_model=list[ResidentResponse])
def get_residents(db: Session = Depends(get_db)):
    return db.query(Resident).all()


@router.get("/{resident_id}", response_model=ResidentResponse)
def get_resident(
    resident_id: int,
    db: Session = Depends(get_db),
):
    resident = (
        db.query(Resident)
        .filter(Resident.resident_id == resident_id)
        .first()
    )

    if resident is None:
        raise HTTPException(
            status_code=404,
            detail="Resident not found",
        )

    return resident