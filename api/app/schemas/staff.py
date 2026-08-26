from datetime import datetime

from pydantic import BaseModel, ConfigDict


class StaffCreate(BaseModel):
    full_name: str
    email: str
    role: str


class StaffResponse(StaffCreate):
    model_config = ConfigDict(from_attributes=True)

    staff_id: int
    is_active: bool
    created_at: datetime