from fastapi import APIRouter
from app.schemas import AnalyzeQuoteRequest, AnalyzeQuoteResponse
from app.services.quote_analyzer import analyze_quote

router = APIRouter()


@router.post("/analyze-quote", response_model=AnalyzeQuoteResponse)
def analyze_quote_endpoint(payload: AnalyzeQuoteRequest):
    return analyze_quote(payload)
