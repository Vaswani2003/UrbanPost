from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from src.core.logging import logger
from src.core.config import get_config_settings
import time
from datetime import datetime, timezone
import sys

from src.models.test_db import TestDB

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
    
@monitoring_router.post("/test_db_write")
async def test_db_write():
    """
    Test database write operation using Beanie ODM.
    This endpoint is used to verify that the database is operational by writing a test document.
    """
    try:
       
        test_doc = TestDB(
            name="API Test Entry",
            purpose="Testing database connection via API endpoint"
        )
        
        await test_doc.insert()

        logger.info(f"Test document created with ID: {test_doc.id}")
        
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": "Test document created successfully", 
                "id": str(test_doc.id),
                "name": test_doc.name,
                "created_at": test_doc.created_at.isoformat()
            }
        )
    
    except Exception as e:
        logger.error(f"Test DB write failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Test DB write failed: {str(e)}"
        )

@monitoring_router.get("/test_db_read")
async def test_db_read():
    """
    Test database read operation using Beanie ODM.
    This endpoint retrieves all test documents to verify database operations.
    """
    try:
        # Get all test documents
        test_docs = await TestDB.find_all().to_list()
        
        logger.info(f"Retrieved {len(test_docs)} test documents")
        
        docs_data = []

        for doc in test_docs:
            docs_data.append({
                "id": str(doc.id),
                "name": doc.name,
                "purpose": doc.purpose,
                "created_at": doc.created_at.isoformat()
            })
        
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": f"Retrieved {len(test_docs)} test documents",
                "count": len(test_docs),
                "documents": docs_data
            }
        )
    
    except Exception as e:
        logger.error(f"Test DB read failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Test DB read failed: {str(e)}"
        )

@monitoring_router.delete("/test_db_cleanup")
async def test_db_cleanup():
    """
    Clean up test documents from database.
    This endpoint removes all test documents to keep the database clean.
    """
    try:
        result = await TestDB.delete_all()
        
        logger.info(f"Deleted {result.deleted_count} test documents")
        
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": f"Deleted {result.deleted_count} test documents",
                "deleted_count": result.deleted_count
            }
        )
    
    except Exception as e:
        logger.error(f"Test DB cleanup failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Test DB cleanup failed: {str(e)}"
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


