import logging
from abc import ABC, abstractmethod

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection as Collection

from src.config import Config

logger = logging.getLogger(__name__)


class BaseRepository(ABC):
    @abstractmethod
    async def create_one(self, collection: str, data: dict):
        """
        create one record in db

        :param collection: name of collection
        :param data: new record
        """
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, collection: str, filter: dict, new_data: dict):
        """
        update one record by filter

        :param collection: Name of collection
        :param filter: query
        :param new_data: new record
        """
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, collection: str, filter: dict):
        """
        delete one record by filter

        :param collection: Name of collection
        :param filter: query
        """
        raise NotImplementedError

    @abstractmethod
    async def delete_many(self, collection: str, filter: dict):
        """
        delete records by filter

        :param collection: Name of collection
        :param filter: query
        """
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, collection: str, filter: dict):
        """
        get record from collection by filter

        :param collection: Name of collection
        :param filter: query
        """
        raise NotImplementedError


class MongoRepository(BaseRepository):
    def __init__(self):
        self._database = AsyncIOMotorClient(Config.MONGO_URL)
        self._current_db = self._database["sample_db"]

    async def create_one(self, collection: str, data: dict):
        try:
            collection: Collection = self._current_db[collection]
            obj = await collection.insert_one(data)
            return obj
        except Exception as e:
            logger.error(f"Error occurred in repository(create_one) - {e}")

    async def update_one(self, collection: str, filter: dict, new_data: dict):
        try:
            collection: Collection = self._current_db[collection]
            obj = await collection.update_one(filter=filter, update={"$set": new_data})
            return obj
        except Exception as e:
            logger.error(f"Error occurred in repository(update_one) - {e}")

    async def get_one(self, collection: str, filter: dict):
        try:
            collection: Collection = self._current_db[collection]
            obj = await collection.find_one(filter=filter)
            return obj
        except Exception as e:
            logger.error(f"Error occurred in repository(get_one) - {e}")

    async def delete_many(self, collection: str, filter: dict):
        try:
            collection: Collection = self._current_db[collection]
            obj = await collection.delete_many(filter=filter)
            return obj
        except Exception as e:
            logger.error(f"Error occurred in repository(delete_many) - {e}")

    async def delete_one(self, collection: str, filter: dict):
        try:
            collection: Collection = self._current_db[collection]
            obj = await collection.delete_one(filter=filter)
            return obj
        except Exception as e:
            logger.error(f"Error occurred in repository(delete_one) - {e}")

    async def find_all(self, collection):
        try:
            collection: Collection = self._current_db[collection]
            return collection.find()
        except Exception as e:
            logger.error(f"Error occurred in repository(find) - {e}")


db_repository = MongoRepository()
