from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.facility import Facility
from app.schemas.facility import FacilityCreate, FacilityResponse


router = APIRouter(
    prefix="/facilities",
    tags=["Facilities"],
)


@router.post("", response_model=FacilityResponse, status_code=201)
def create_facility(
    facility: FacilityCreate,
    db: Session = Depends(get_db),
):
    new_facility = Facility(
        name=facility.name,
        suburb=facility.suburb,
        state=facility.state,
    )

    db.add(new_facility)
    db.commit()
    db.refresh(new_facility)

    return new_facility


@router.get("", response_model=list[FacilityResponse])
def get_facilities(db: Session = Depends(get_db)):
    return db.query(Facility).all()