from datetime import datetime

from pydantic import BaseModel, ConfigDict


class FacilityCreate(BaseModel):
    name: str
    suburb: str
    state: str


class FacilityResponse(FacilityCreate):
    model_config = ConfigDict(from_attributes=True)

    facility_id: int
    created_at: datetime