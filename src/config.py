import os

class Config:
    """Конфиг с переменными"""
    MONGO_URL = os.getenv("MONGO_URI")
    TOKEN = os.getenv("TOKEN")