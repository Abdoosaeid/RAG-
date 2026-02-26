from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str 
    APP_version: str
    API_KEY: str
    FILE_ALLOWED_TYPES: list 
    FILE_MAX_SIZE: int
    file_default_chunk_size: int
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

def get_settings():
    return Settings()        