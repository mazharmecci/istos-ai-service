from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "ISTOS AI Service"
    API_VERSION: str = "1.0.0"
    ENV: str = "development"

    class Config:
        env_file = ".env"


settings = Settings()
