"""
Base repository class providing common database operations for Beanie documents.
"""
from typing import Type, TypeVar, Generic, Optional, List, Dict, Any
from beanie import Document, PydanticObjectId
from pymongo import ASCENDING, DESCENDING
from src.core.logging import logger

DocumentType = TypeVar("DocumentType", bound=Document)

class BaseRepository(Generic[DocumentType]):
    """
    Generic base repository providing common CRUD operations for Beanie documents.
    """
    
    def __init__(self, model: Type[DocumentType]):
        self.model = model
    
    async def create(self, **kwargs) -> DocumentType:
        """Create a new document"""
        try:
            document = self.model(**kwargs)
            await document.insert()
            logger.info(f"Created {self.model.__name__} with ID: {document.id}")
            return document
        except Exception as e:
            logger.error(f"Error creating {self.model.__name__}: {e}")
            raise
    
    async def get_by_id(self, id: PydanticObjectId) -> Optional[DocumentType]:
        """Get document by ID"""
        try:
            return await self.model.get(id)
        except Exception as e:
            logger.error(f"Error getting {self.model.__name__} by ID {id}: {e}")
            raise
    
    async def get_all(
        self, 
        skip: int = 0, 
        limit: int = 100,
        sort_by: str = "created_at",
        sort_order: int = DESCENDING
    ) -> List[DocumentType]:
        """Get all documents with pagination"""
        try:
            return await self.model.find_all().skip(skip).limit(limit).sort([(sort_by, sort_order)]).to_list()
        except Exception as e:
            logger.error(f"Error getting all {self.model.__name__}: {e}")
            raise
    
    async def update_by_id(self, id: PydanticObjectId, update_data: Dict[str, Any]) -> Optional[DocumentType]:
        """Update document by ID"""
        try:
            document = await self.get_by_id(id)
            if document:
                for key, value in update_data.items():
                    setattr(document, key, value)
                await document.save()
                logger.info(f"Updated {self.model.__name__} with ID: {id}")
                return document
            return None
        except Exception as e:
            logger.error(f"Error updating {self.model.__name__} with ID {id}: {e}")
            raise
    
    async def delete_by_id(self, id: PydanticObjectId) -> bool:
        """Delete document by ID"""
        try:
            document = await self.get_by_id(id)
            if document:
                await document.delete()
                logger.info(f"Deleted {self.model.__name__} with ID: {id}")
                return True
            return False
        except Exception as e:
            logger.error(f"Error deleting {self.model.__name__} with ID {id}: {e}")
            raise
    
    async def find_by_field(self, field: str, value: Any) -> List[DocumentType]:
        """Find documents by a specific field value"""
        try:
            return await self.model.find({field: value}).to_list()
        except Exception as e:
            logger.error(f"Error finding {self.model.__name__} by {field}: {e}")
            raise
    
    async def count(self, filter_dict: Optional[Dict[str, Any]] = None) -> int:
        """Count documents with optional filter"""
        try:
            if filter_dict:
                return await self.model.find(filter_dict).count()
            return await self.model.find_all().count()
        except Exception as e:
            logger.error(f"Error counting {self.model.__name__}: {e}")
            raise
    
    async def exists(self, filter_dict: Dict[str, Any]) -> bool:
        """Check if document exists with given filter"""
        try:
            document = await self.model.find_one(filter_dict)
            return document is not None
        except Exception as e:
            logger.error(f"Error checking existence of {self.model.__name__}: {e}")
            raise
