from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import analyze_quote

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION
)

# ============================
# CORS Middleware
# ============================
# For initial testing, allow GitHub Pages domain
origins = [
    "https://mazharmecci.github.io",  # your GitHub Pages domain
    "http://localhost:3000"           # optional for local dev/testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # you can use ["*"] for all origins temporarily
    allow_credentials=True,
    allow_methods=["*"],        # allow all HTTP methods
    allow_headers=["*"]         # allow all headers
)

# ============================
# Health check endpoint
# ============================
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": settings.APP_NAME,
        "environment": settings.ENV
    }

# ============================
# Include analyze-quote router
# ============================
app.include_router(analyze_quote.router, prefix="", tags=["AI"])
