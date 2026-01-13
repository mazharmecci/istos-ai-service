from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers.analyze_quote import router as analyze_quote_router

<<<<<<< HEAD

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.API_VERSION,
    )

=======
def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.API_VERSION,
    )

>>>>>>> 70ca588b10df2594cbe022713b5891cc4c7e163d
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

<<<<<<< HEAD
=======
    # mount /analyze-quote
    app.include_router(analyze_quote_router)

>>>>>>> 70ca588b10df2594cbe022713b5891cc4c7e163d
    return app


app = create_app()
