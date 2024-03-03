from .base import MongoRepository
from src.database.dto.salary import Salary

class SalaryRepository(MongoRepository):
    """
    Репозиторий для CRUD операций с зарплатами людей
    """
    def __init__(self):
        super().__init__()

    async def get_all_salaries(self) -> list[Salary]:
        pass
