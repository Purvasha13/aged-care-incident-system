from sqlalchemy import Column, ForeignKey, Integer, String, Time

from app.database import Base


class StaffAvailability(Base):
    __tablename__ = "staff_availability"

    availability_id = Column(Integer, primary_key=True)

    staff_id = Column(
        Integer,
        ForeignKey("staff.staff_id"),
        nullable=False,
    )

    day_of_week = Column(String(10), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)