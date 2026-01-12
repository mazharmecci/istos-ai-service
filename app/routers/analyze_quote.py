from fastapi import APIRouter
from app.schemas import QuoteAnalysisRequest, QuoteAnalysisResponse

router = APIRouter()

@router.post("/analyze-quote", response_model=QuoteAnalysisResponse)
def analyze_quote(payload: QuoteAnalysisRequest):
    """
    MOCK AI RESPONSE – ready for Day 8
    This placeholder will be replaced by real AI models later.
    """

    # Extract fields from payload
    deal_value = payload.quote.deal_value
    avg_price = payload.historical_context.avg_winning_price

    # Simple heuristic logic for demo
    if deal_value < avg_price:
        pricing_risk = "Medium"
        win_probability = 72
    else:
        pricing_risk = "Low"
        win_probability = 85

    # Key risks and recommendations
    key_risks = [
        "Pricing slightly deviates from historical average",
        "Private hospital shows moderate price sensitivity"
    ]
    recommended_focus = "Emphasize value and service reliability over discounts"

    return QuoteAnalysisResponse(
        win_probability=win_probability,
        pricing_risk=pricing_risk,
        key_risks=key_risks,
        recommended_focus=recommended_focus
    )
