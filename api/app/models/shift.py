from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, Time
from sqlalchemy.sql import func

from app.database import Base


class Shift(Base):
    __tablename__ = "shifts"

    shift_id = Column(Integer, primary_key=True)

    facility_id = Column(
        Integer,
        ForeignKey("facilities.facility_id"),
        nullable=False,
    )

    shift_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    required_role = Column(String(50), nullable=False)
    status = Column(String(20), nullable=False, default="OPEN")

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )