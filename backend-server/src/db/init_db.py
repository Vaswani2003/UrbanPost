"""
Database initialization module for Citizens Issues Registry.
Sets up MongoDB connection with Beanie ODM and initializes all document models.
"""
import motor.motor_asyncio
from beanie import init_beanie
from src.core.config import get_config_settings
from src.core.logging import logger

# Import all document models
from src.models import TestDB

config = get_config_settings()

class Database:
    """Singleton database connection manager"""
    _instance = None
    _initialized = False

    def __init__(self):
        if Database._instance is not None:
            raise Exception("This class is a singleton! Use Database.get_instance()")
        self.client: motor.motor_asyncio.AsyncIOMotorClient = None
        self.database: motor.motor_asyncio.AsyncIOMotorDatabase = None

    @classmethod
    async def get_instance(cls):
        """Get singleton instance and initialize if needed"""
        if cls._instance is None:
            cls._instance = Database()
            await cls._instance._connect()
        return cls._instance

    @logger.catch
    async def _connect(self):
        """Private method to establish database connection"""
        if self._initialized:
            return
            
        self.client = motor.motor_asyncio.AsyncIOMotorClient(
            config.DATABASE_URL,
            maxPoolSize=config.MAX_CONNECTIONS_COUNT,
            minPoolSize=config.MIN_CONNECTIONS_COUNT,
        )

        self.database = self.client[config.DATABASE_NAME]
        
        await self.client.admin.command('ping')
        logger.info(f"Connected to MongoDB successfully at {config.DATABASE_URL}")
        
        await init_beanie(
            database=self.database,
            document_models=[TestDB]
        )
        
        logger.info("Beanie ODM initialized successfully")
        Database._initialized = True

    @logger.catch
    async def close_connection(self):
        """Close database connection"""
        if self.client:
            self.client.close()
            logger.info("Disconnected from MongoDB")
            Database._initialized = False

    def get_database(self):
        """Get database instance"""
        return self.database


async def initialize_database():
    """Initialize the database connection and Beanie ODM"""
    await Database.get_instance()
    logger.info("Database initialization completed")

async def close_mongo_connection():
    """Close database connection"""
    if Database._instance:
        await Database._instance.close_connection()

def get_database():
    """Get database instance"""
    if Database._instance:
        return Database._instance.get_database()
    return None
