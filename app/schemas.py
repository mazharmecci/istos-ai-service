from pydantic import BaseModel
from typing import List, Optional


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
    items: List[QuoteItem] = []


class HistoricalContext(BaseModel):
    avg_winning_price: float
    similar_quotes_won: int = 0
    similar_quotes_lost: int = 0


class AnalyzeQuoteRequest(BaseModel):
    quote: Quote
    historical_context: HistoricalContext


class AnalyzeQuoteResponse(BaseModel):
    win_probability: int
    pricing_risk: str
    key_risks: List[str]
    recommended_focus: str
