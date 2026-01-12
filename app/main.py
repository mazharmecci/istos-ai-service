from fastapi import FastAPI
from app.routers.analyze import router as analyze_router

app = FastAPI(title="ISTOS AI Service")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "ISTOS AI Service",
        "environment": "production"
    }

app.include_router(analyze_router)
