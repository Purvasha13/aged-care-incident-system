from fastapi import FastAPI

from app.config import APP_ENV, APP_VERSION

from app.database import check_database_connection

app = FastAPI(
    title="Secure Aged Care Cloud Platform",
    description=(
        "Cloud-native aged care platform for resident operations, "
        "workforce rostering, security, and reliability engineering."
    ),
    version=APP_VERSION,
)


@app.get("/")
def root():
    return {
        "service": "Secure Aged Care Cloud Platform",
        "message": "API is running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "secure-aged-care-cloud-platform",
    }


@app.get("/version")
def version():
    return {
        "version": APP_VERSION,
        "environment": APP_ENV,
    }

@app.get("/db-health")
def database_health():
    return check_database_connection()