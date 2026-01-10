from app.schemas import (
    QuoteAnalysisRequest,
    QuoteAnalysisResponse,
)
from app.core.logging import get_logger

logger = get_logger("quote_analyzer")


def analyze_quote_ai(payload: QuoteAnalysisRequest) -> QuoteAnalysisResponse:
    """
    Core AI decision logic.
    Currently heuristic-based (Phase 1).
    Replace with ML / LLM inference in later phases.
    """

    logger.info(
        "Analyzing quote",
        extra={"deal_value": payload.quote.deal_value},
    )

    deal_value = payload.quote.deal_value
    avg_price = payload.historical_context.avg_winning_price

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
            "Private hospital shows moderate price sensitivity",
        ],
        recommended_focus="Emphasize value and service reliability over discounts",
    )
