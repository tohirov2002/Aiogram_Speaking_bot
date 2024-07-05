from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
import logging
import sys
import asyncio

from config import TOKEN
from handlers.msg_handlers import msg_router


async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    db = Dispatcher()
    db.include_router(msg_router)
    await db.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
