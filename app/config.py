import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "ISTOS AI Service"
    ENV = os.getenv("ENV", "development")
    API_VERSION = "v1"

settings = Settings()

