from fastapi import FastAPI

app = FastAPI(
    title="Secure Aged Care Cloud Platform",
    description=(
        "Cloud-native aged care platform for resident operations, "
        "workforce rostering, security, and reliability engineering."
    ),
    version="0.1.0",
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
        "version": "0.1.0",
        "environment": "development",
    }