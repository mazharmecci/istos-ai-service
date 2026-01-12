from pydantic import BaseModel, Field
from typing import List, Optional

# ----------------------------
# Quote and Historical Context
# ----------------------------

class QuoteItem(BaseModel):
    item_id: str
    quantity: int
    unit_price: float
    description: Optional[str] = None

class Quote(BaseModel):
    deal_value: float
    hospital: str
    instrument_category: str
    configuration_complexity: str
    items: Optional[List[QuoteItem]] = []

class HistoricalContext(BaseModel):
    avg_winning_price: float
    similar_quotes_won: Optional[int] = 0
    similar_quotes_lost: Optional[int] = 0

# ----------------------------
# Request & Response Schemas
# ----------------------------

class QuoteAnalysisRequest(BaseModel):
    quote: Quote
    historical_context: HistoricalContext

class QuoteAnalysisResponse(BaseModel):
    win_probability: int = Field(..., ge=0, le=100)
    pricing_risk: str
    key_risks: List[str]
    recommended_focus: str
