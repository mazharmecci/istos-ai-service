from fastapi import FastAPI

from app.config import settings
from app.schemas import (
    QuoteAnalysisRequest,
    QuoteAnalysisResponse,
)

# ------------------------------------------------------------------
# FastAPI App Initialization
# ------------------------------------------------------------------

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION,
)

# ------------------------------------------------------------------
# Root & Health Endpoints
# ------------------------------------------------------------------

@app.get("/")
def root():
    return {
        "status": "ISTOS AI Service running",
        "service": settings.APP_NAME,
        "environment": settings.ENV,
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": settings.APP_NAME,
        "environment": settings.ENV,
    }

# ------------------------------------------------------------------
# Quote Analysis (Mock AI – Phase 1)
# ------------------------------------------------------------------

from app.services.quote_analyzer import analyze_quote_ai

@app.post("/analyze-quote", response_model=QuoteAnalysisResponse)
def analyze_quote(payload: QuoteAnalysisRequest):
    return analyze_quote_ai(payload)
