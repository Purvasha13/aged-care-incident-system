from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from app.config import DATABASE_URL


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)


def check_database_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "database": "connected",
            "status": "healthy",
        }

    except SQLAlchemyError as error:
        return {
            "database": "disconnected",
            "status": "error",
            "message": str(error),
        }