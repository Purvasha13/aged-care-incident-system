from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.config import APP_ENV, APP_VERSION
from app.database import check_database_connection, get_db
from app.models.resident import Resident
from app.schemas.resident import ResidentCreate, ResidentResponse

app = FastAPI(
    title="Secure Aged Care Cloud Platform",
    description=(
        "Cloud-native aged care platform for resident operations, "
        "workforce rostering, security, and reliability engineering."
    ),
    version=APP_VERSION,
)


@app.get("/")
def root():
    return {
        "service": "Secure Aged Care Cloud Platform",
        "message": "API is running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "secure-aged-care-cloud-platform",
    }


@app.get("/version")
def version():
    return {
        "version": APP_VERSION,
        "environment": APP_ENV,
    }

@app.get("/db-health")
def database_health():
    return check_database_connection()

@app.post("/residents", response_model=ResidentResponse, status_code=201)
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