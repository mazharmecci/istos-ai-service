from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import QuoteAnalysisRequest, QuoteAnalysisResponse
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://mazharmecci.github.io",
        "https://qms.istosmedical.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": settings.APP_NAME,
        "environment": settings.ENV
    }
