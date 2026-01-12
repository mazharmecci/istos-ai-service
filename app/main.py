from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.analyze import router as analyze_router

app = FastAPI(title="ISTOS AI Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://mazharmecci.github.io",
        "https://qms.istosmedical.com",
        "https://ai.istosmedical.com",  # Add this
        "http://localhost:3000",       # Add for dev
        "*"                            # Temp for testing (remove production)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze_router)  # Routers after middleware

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "ISTOS AI Service",
        "environment": "production"
    }
