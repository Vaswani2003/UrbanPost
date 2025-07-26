from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from src.core.logging import logger
from src.core.config import get_config_settings
import time
from datetime import datetime, timezone
import sys

monitoring_router = APIRouter(
    prefix="/monitoring",
    tags=["Monitoring"]
)

# Store application start time
app_start_time = time.time()
config = get_config_settings()

@monitoring_router.get("/health", 
                      summary="Basic Health Check",
                      description="Simple health check endpoint for load balancers and basic monitoring")
async def health_check():
    """
    Basic health check endpoint that returns a simple status.
    Typically used by load balancers and container orchestrators.
    """
    try:
        current_time = datetime.now(timezone.utc).isoformat()
        uptime = time.time() - app_start_time
        
        logger.debug(f"Health check performed at {current_time}")
        
        return {
            "status": "healthy",
            "timestamp": current_time,
            "uptime_seconds": round(uptime, 2)
        }
    
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Health check failed"
        )

@monitoring_router.get("/status",
                      summary="Detailed Status Check", 
                      description="Comprehensive status endpoint with system metrics and application details")
async def status_check():
    """
    Basic status check without psutil dependencies.
    """
    try:
        current_time = datetime.now(timezone.utc).isoformat()
        uptime = time.time() - app_start_time
        
        # Application info
        app_info = {
            "name": config.TITLE,
            "version": config.VERSION,
            "environment": getattr(config, 'ENVIRONMENT', 'unknown'),
            "python_version": sys.version,
            "host": config.HOST,
            "port": config.PORT
        }
        
        logger.info("Status check performed")
        
        response_data = {
            "status": "healthy",
            "timestamp": current_time,
            "uptime_seconds": round(uptime, 2),
            "uptime_human": format_uptime(uptime),
            "application": app_info
        }
        
        return response_data
        
    except Exception as e:
        logger.error(f"Status check failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Status check failed: {str(e)}"
        )

# Helper functions
def format_uptime(uptime_seconds: float) -> str:
    """Format uptime in human-readable format."""
    days = int(uptime_seconds // 86400)
    hours = int((uptime_seconds % 86400) // 3600)
    minutes = int((uptime_seconds % 3600) // 60)
    seconds = int(uptime_seconds % 60)
    
    if days > 0:
        return f"{days}d {hours}h {minutes}m {seconds}s"
    elif hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    elif minutes > 0:
        return f"{minutes}m {seconds}s"
    else:
        return f"{seconds}s"


