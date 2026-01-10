from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.config import settings
from app.schemas import (
    QuoteAnalysisRequest,
    QuoteAnalysisResponse,
)

from app.services.quote_analyzer import analyze_quote_ai

# ------------------------------------------------------------------
# FastAPI App Initialization
# ------------------------------------------------------------------

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION,
)

# ------------------------------------------------------------------
# Global Exception Handler
# ------------------------------------------------------------------

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": str(exc),
        },
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

@app.post("/v1/analyze-quote", response_model=QuoteAnalysisResponse)
def analyze_quote(payload: QuoteAnalysisRequest):
    return analyze_quote_ai(payload)

