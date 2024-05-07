import json
import logging
from datetime import datetime

from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from src.database.repositories.salary import SalaryRepository
from src.usecases.salaries.payments import AggregatePayments

logger = logging.getLogger(__name__)

router = Router(name="main")


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@router.message()
async def echo_handler(message: types.Message) -> None:
    try:
        message_json = json.loads(message.text)
        dt_from = datetime.fromisoformat(message_json["dt_from"])
        dt_upto = datetime.fromisoformat(message_json["dt_upto"])
        command = AggregatePayments(SalaryRepository())
        payments = await command.execute(
            dt_from, dt_upto, message_json["group_type"]
        )
        await message.answer(json.dumps(payments))

    except Exception as e:
        logger.error(f"Got an unexpected error - {e}")
