import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str
    CORS_ORIGINS: str 
    EMAIL_ADDRESS:str
    EMAIL_PASSWORD:str
    RECIPIENT_EMAIL: str
    APP_PORT: int

    class Config:
        env_file = "./.env"
        env_file_encoding = "utf-8"


settings = Settings()

# Convert comma-separated string → proper list
ALLOWED_ORIGINS = [origin.strip() for origin in settings.CORS_ORIGINS.split(",")]
