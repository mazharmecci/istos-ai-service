from fastapi import FastAPI
from app.config import settings
from app.routers import analyze_quote

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION
)

# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": settings.APP_NAME,
        "environment": settings.ENV
    }

# Include analyze-quote router
app.include_router(analyze_quote.router, prefix="", tags=["AI"])
