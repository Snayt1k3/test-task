import logging

from .base import MongoRepository
from src.database.dto.salary import Salary

logger = logging.getLogger(__name__)


class SalaryRepository(MongoRepository):
    """
    Репозиторий для операций с зарплатами людей
    """

    def __init__(self):
        super().__init__()
        self._current_db = self._database["salaries"]

    async def get_all_salaries(self, collection: str) -> list[Salary]:
        try:
            data = await self.find_all(collection)
            output = []
            async for obj in data:
                output.append(Salary(obj["value"], obj["dt"]))

            return output
        except Exception as e:
            logger.error(
                f"Error occurred in salary repositories(get_all_salaries) - {e}"
            )
            return []


salary_db = SalaryRepository()
