import sys, os
project_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_path)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.config import get_config_settings
from src.core.case_conversion_middleware import CaseConversionMiddleware
from src.core.logging import logger
from src.routers.monitoring import monitoring_router

config = get_config_settings()

# ========================================= LIFESPAN ========================================================

async def lifespan(app: FastAPI):
    logger.info("Starting Citizens Issues Registry Backend Server...")
    logger.info(f"Server configuration loaded - Environment: {getattr(config, 'ENVIRONMENT', 'development')}")
    logger.info(f"API Documentation available at: {config.DOCS_URL}")
    yield
    logger.info("Shutting down Citizens Issues Registry Backend Server...")
    logger.info("Server stopped gracefully")


app = FastAPI(
    title=config.TITLE,
    description=config.DESCRIPTION,
    version=config.VERSION,
    openapi_url=config.OPENAPI_URL,
    docs_url=config.DOCS_URL,
    redoc_url=config.REDOC_URL,
    contact=config.CONTACT,
    lifespan=lifespan
)

# ========================================= MIDDLEWARES ========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=config.CORS_ALLOW_CREDENTIALS,
    allow_methods=config.CORS_ALLOW_METHODS,
    allow_headers=config.CORS_ALLOW_HEADERS
)

app.add_middleware(CaseConversionMiddleware)

# ========================================= ROUTES ========================================================

app.include_router(monitoring_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=config.HOST, 
        port=config.PORT,
        reload=True,
        reload_dirs=["src"],  
        log_level="info"
    )
