import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.enums import ParseMode
from src.bot import TOKEN, dp
from src.handlers.main import router


async def main() -> None:
    dp.include_router(router)
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
