from beanie import Document
from pydantic import Field
from datetime import datetime

from .collections import Collections

class TestDB(Document):
    """Test database model for demonstration purposes"""
    
    name: str = Field(..., description="Name of the test entry")
    purpose: str = Field(..., description="Purpose of the test entry")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    
    class Settings:
        name = Collections.HEALTH_TEST
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Sample Entry",
                "purpose": "This is a sample entry for testing purposes",
                "created_at": "2023-10-01T12:00:00Z"
            }
        }