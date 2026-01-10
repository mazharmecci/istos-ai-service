from pydantic import BaseModel, Field
from typing import List, Optional


class Hospital(BaseModel):
    name: str
    segment: str = Field(example="Private")
    city_tier: int = Field(example=2)
    bed_count: Optional[int]


class Quote(BaseModel):
    deal_value: float = Field(example=4800000)
    instrument_category: str = Field(example="Histopathology")
    configuration_complexity: str = Field(example="High")


class HistoricalContext(BaseModel):
    similar_quotes_won: int
    similar_quotes_lost: int
    avg_winning_price: float


class QuoteAnalysisRequest(BaseModel):
    hospital: Hospital
    quote: Quote
    historical_context: HistoricalContext


class QuoteAnalysisResponse(BaseModel):
    win_probability: int = Field(ge=0, le=100)
    pricing_risk: str
    key_risks: List[str]
    recommended_focus: str

