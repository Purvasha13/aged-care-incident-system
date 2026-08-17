from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


class ResidentCreate(BaseModel):
    full_name: str
    date_of_birth: date
    room_number: str | None = None
    emergency_contact: str | None = None


class ResidentResponse(ResidentCreate):
    model_config = ConfigDict(from_attributes=True)

    resident_id: int
    created_at: datetime