import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
import logging

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply('Привет!')
    await message.answer('Как дела?')
    await message.answer_photo(photo='https://sudoteach.com/static/assets/img/aiogram-banner.jpg', caption='Лучший курс по aiogram!')


@dp.message()
async def echo(message: Message):
    await message.answer('Это неизвестная команда.')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO) # Подключение логирования
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')