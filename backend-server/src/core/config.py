from pydantic_settings import BaseSettings
from typing import Dict, Any
from functools import lru_cache

class ConfigSettings(BaseSettings):
    
    # APP settings
    TITLE: str = "Citizens Issues Repository Backend"
    DESCRIPTION: str = "This is a FastAPI based backend for managing citizen issues, complaints, and suggestions. The application provides endpoints for CRUD operations on issues, user management, and more."
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
    HOST: str = "localhost"

    # CORS settings
    CORS_ORIGINS: list[str] = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: list[str] = ["*"]
    CORS_ALLOW_HEADERS: list[str] = ["*"]

    # Logger Configuration
    LOG_DIRECTORY: str = "logs"
    LOG_FILE: str = "cir_backend.log"
    LOG_LEVEL: str = "DEBUG"
    LOG_ROTATION: str = "10 MB"
    LOG_RETENTION: str = "10 days"
    LOG_COMPRESSION: str = "zip"
    LOG_COLORIZE: bool = True
    LOG_ENQUEUE: bool = True
    LOG_BACKTRACE: bool = True
    LOG_DIAGNOSE: bool = True
    LOG_FORMAT: str = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{message}</cyan>"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


@lru_cache()
def get_config_settings() -> ConfigSettings:
    return ConfigSettings()