import logging
import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router
from app.loadenv import envi

async def main():
    bot = Bot(token=envi.token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except Exception:
        print('Exit')