from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.staff import Staff
from app.schemas.staff import StaffCreate, StaffResponse


router = APIRouter(
    prefix="/staff",
    tags=["Staff"],
)


@router.post("", response_model=StaffResponse, status_code=201)
def create_staff(
    staff: StaffCreate,
    db: Session = Depends(get_db),
):
    new_staff = Staff(
        full_name=staff.full_name,
        email=staff.email,
        role=staff.role,
    )

    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)

    return new_staff


@router.get("", response_model=list[StaffResponse])
def get_staff(db: Session = Depends(get_db)):
    return db.query(Staff).all()