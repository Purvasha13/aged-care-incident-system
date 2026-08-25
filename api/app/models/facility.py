from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database import Base


class Facility(Base):
    __tablename__ = "facilities"

    facility_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    suburb = Column(String(100), nullable=False)
    state = Column(String(50), nullable=False)
    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )