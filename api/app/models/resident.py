from sqlalchemy import Column, Date, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database import Base


class Resident(Base):
    __tablename__ = "residents"

    resident_id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    room_number = Column(String(20), nullable=True)
    emergency_contact = Column(String(100), nullable=True)
    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )