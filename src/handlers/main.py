from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

router = Router(name="main")

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@router.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
