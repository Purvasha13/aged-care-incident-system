from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func

from app.database import Base


class Assignment(Base):
    __tablename__ = "assignments"

    assignment_id = Column(Integer, primary_key=True)

    staff_id = Column(
        Integer,
        ForeignKey("staff.staff_id"),
        nullable=False,
    )

    shift_id = Column(
        Integer,
        ForeignKey("shifts.shift_id"),
        nullable=False,
    )

    status = Column(
        String(20),
        nullable=False,
        default="ASSIGNED",
    )

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )