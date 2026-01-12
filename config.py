import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str
    BREVO_API_KEY: str
    SENDER_EMAIL: str
    RECIPIENT_EMAIL: str
    APP_PORT: int
    CORS_ORIGINS: str
    
    class Config:
        env_file = "./.env"
        env_file_encoding = "utf-8"
        case_sensitive = False
    
    @property
    def cors_origins_list(self):
        """Convert comma-separated string to list"""
        return [url.strip() for url in self.CORS_ORIGINS.split(",")]

settings = Settings()

# Debug output
print("=" * 50)
print("✓ Config loaded!")
print("PORT", settings.APP_PORT)
print(f"✓ BREVO_API_KEY: {settings.BREVO_API_KEY[:15]}...")
print(f"✓ SENDER_EMAIL: {settings.SENDER_EMAIL}")
print(f"✓ RECIPIENT_EMAIL: {settings.RECIPIENT_EMAIL}")
print(f"✓ CORS_ORIGINS: {settings.cors_origins_list}")
print("=" * 50)



# import os
# from pydantic_settings import BaseSettings
# from pydantic import Field

# class Settings(BaseSettings):
#     PROJECT_NAME: str
#     CORS_ORIGINS: str
#     BREVO_API_KEY: str
#     SENDER_EMAIL: str
#     RECIPIENT_EMAIL: str
#     APP_PORT: int
    
#     class Config:
#         env_file = "./.env"
#         env_file_encoding = "utf-8"
#         # This makes it case-insensitive
#         case_sensitive = False

# settings = Settings()


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


