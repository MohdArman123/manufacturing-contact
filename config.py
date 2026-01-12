import os
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    PROJECT_NAME: str
    CORS_ORIGINS: str
    BREVO_API_KEY: str
    SENDER_EMAIL: str
    RECIPIENT_EMAIL: str
    APP_PORT: int
    
    class Config:
        env_file = "./.env"
        env_file_encoding = "utf-8"
        # This makes it case-insensitive
        case_sensitive = False

settings = Settings()


# import os
# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     PROJECT_NAME: str
#     CORS_ORIGINS: list[str]
#     CORS_ORIGINS: str 
#     EMAIL_ADDRESS:str
#     EMAIL_PASSWORD:str
#     RECIPIENT_EMAIL: str
#     APP_PORT: int

#     class Config:
#         env_file = "./.env"
#         env_file_encoding = "utf-8"


# settings = Settings()

