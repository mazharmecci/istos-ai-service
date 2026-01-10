from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ISTOS AI Service running"}

from app.schemas import (
    QuoteAnalysisRequest,
    QuoteAnalysisResponse
)
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": settings.APP_NAME,
        "environment": settings.ENV
    }


@app.post("/analyze-quote", response_model=QuoteAnalysisResponse)
def analyze_quote(payload: QuoteAnalysisRequest):
    """
    MOCK AI RESPONSE – Day 7 only
    This will be replaced by real AI logic later.
    """

    deal_value = payload.quote.deal_value
    avg_price = payload.historical_context.avg_winning_price

    # Simple heuristic (temporary)
    if deal_value < avg_price:
        pricing_risk = "Medium"
        win_probability = 72
    else:
        pricing_risk = "Low"
        win_probability = 85

    return QuoteAnalysisResponse(
        win_probability=win_probability,
        pricing_risk=pricing_risk,
        key_risks=[
            "Pricing slightly deviates from historical average",
            "Private hospital shows moderate price sensitivity"
        ],
        recommended_focus="Emphasize value and service reliability over discounts"
    )

