from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION,
)

@app.get("/")
def root():
    return {
        "status": "ISTOS AI Service running",
        "environment": settings.ENV,
    }
