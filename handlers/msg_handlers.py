from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from aiogram import Router

msg_router = Router()


@msg_router.message()
async def echo(message: Message):
    await message.answer(message.text)