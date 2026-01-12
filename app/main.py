from fastapi import FastAPI
from app.schemas import QuoteAnalysisRequest, QuoteAnalysisResponse
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
    Day 8 – Rule-based AI (Mock logic)
    This will later be replaced by ML models
    """

    quote = payload.quote
    context = payload.historical_context

    deal_value = quote.deal_value
    avg_price = context.avg_winning_price

    if deal_value <= avg_price:
        pricing_risk = "Medium"
        win_probability = 72
    else:
        pricing_risk = "Low"
        win_probability = 85

    return QuoteAnalysisResponse(
        win_probability=win_probability,
        pricing_risk=pricing_risk,
        key_risks=[
            f"Quoted value ₹{deal_value} vs historical avg ₹{avg_price}",
            f"{quote.hospital} is moderately price sensitive"
        ],
        recommended_focus=(
            "Emphasize service reliability and long-term support "
            "rather than price discounts"
        )
    )
