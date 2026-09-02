from datetime import date, datetime, time

from pydantic import BaseModel, ConfigDict


class ShiftCreate(BaseModel):
    facility_id: int
    shift_date: date
    start_time: time
    end_time: time
    required_role: str


class ShiftResponse(ShiftCreate):
    model_config = ConfigDict(from_attributes=True)

    shift_id: int
    status: str
    created_at: datetime