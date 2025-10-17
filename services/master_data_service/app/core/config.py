from pydantic_settings import BaseSettings
from typing import Dict, Any
from functools import lru_cache

class ConfigSettings(BaseSettings):
    
    # APP settings
    TITLE: str = "UrbanPost - MasterData Server Backend"
    DESCRIPTION: str = "A service for managing and processing masterdata."
    VERSION: str = "1.0.0"
    OPENAPI_URL: str = "/api/v1/openapi.json"
    DOCS_URL: str = "/api/v1/docs"
    REDOC_URL: str = "/api/v1/redoc"
    CONTACT: Dict = {
        "name": "Vinamra Vaswani",
        "email": "vinamravaswani@gmail.com"
    }
    ENVIRONMENT: str = "development"

    PORT : int = 8000
    HOST: str = "0.0.0.0"

    # CORS settings
    CORS_ORIGINS: list[str] = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: list[str] = ["*"]
    CORS_ALLOW_HEADERS: list[str] = ["*"]

    # Database Configuration
    DATABASE_URL: str = "mongodb://localhost:27017/UrbanPost"
    DATABASE_NAME: str = "UrbanPost"
    MAX_CONNECTIONS_COUNT: int = 10
    MIN_CONNECTIONS_COUNT: int = 1

    # Logger Configuration
    LOG_DIRECTORY: str = "logs"
    LOG_FILE: str = "master_data.log"
    LOG_LEVEL: str = "DEBUG"
    LOG_ROTATION: str = "10 MB"
    LOG_RETENTION: str = "10 days"
    LOG_COMPRESSION: str = "zip"
    LOG_COLORIZE: bool = True
    LOG_ENQUEUE: bool = True
    LOG_BACKTRACE: bool = True
    LOG_DIAGNOSE: bool = True
    LOG_FORMAT: str = "<green>{time:DD-MM-YYYY HH:mm:ss}</green> | <level>{level}</level> | <cyan>{message}</cyan>"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


@lru_cache()
def get_config_settings() -> ConfigSettings:
    return ConfigSettings()