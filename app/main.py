# /opt/istos-ai-service/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.API_VERSION,
    )

    allowed_origins = [
        "https://mazharmecci.github.io",
        "https://qms.istosmedical.com",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health")
    def health_check() -> dict:
        return {
            "status": "ok",
            "service": settings.APP_NAME,
            "environment": settings.ENV,
        }

    return app


app = create_app()
