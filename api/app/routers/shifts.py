from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.shift import Shift
from app.schemas.shift import ShiftCreate, ShiftResponse


router = APIRouter(
    prefix="/shifts",
    tags=["Shifts"],
)


@router.post("", response_model=ShiftResponse, status_code=201)
def create_shift(
    shift: ShiftCreate,
    db: Session = Depends(get_db),
):
    new_shift = Shift(
        facility_id=shift.facility_id,
        shift_date=shift.shift_date,
        start_time=shift.start_time,
        end_time=shift.end_time,
        required_role=shift.required_role,
        status="OPEN",
    )

    db.add(new_shift)
    db.commit()
    db.refresh(new_shift)

    return new_shift


@router.get("", response_model=list[ShiftResponse])
def get_shifts(db: Session = Depends(get_db)):
    return db.query(Shift).all()


@router.get("/{shift_id}", response_model=ShiftResponse)
def get_shift(
    shift_id: int,
    db: Session = Depends(get_db),
):
    shift = (
        db.query(Shift)
        .filter(Shift.shift_id == shift_id)
        .first()
    )

    if shift is None:
        raise HTTPException(
            status_code=404,
            detail="Shift not found",
        )

    return shift