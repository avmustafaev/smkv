import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import logging

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
kn1pic_id = os.getenv('KN1PIC')
video_note_hello = os.getenv('VNHELLO')
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    # await message.reply('Привет!')
    # await message.answer('Как дела?')
    await message.answer_photo(photo=kn1pic_id, caption='Вы присоединились к боту отчётов KN1')
    #await message.answer_video_note(video_note=video_note_hello)





@dp.message(F.text =='привет!')
async def echo(message: Message):
    await message.answer('ну и тебе тоже')
    
    
@dp.message(F.photo)
async def get_photo(message: Message):
    photo_id = message.photo[-1].file_id
    await message.answer_photo(photo=photo_id)
    await message.answer(f'ID фотографии: {message.photo[-1].file_id}')
    
    
@dp.message(F.video_note)
async def get_round(message: Message):
    roundvid = message.video_note.file_id
    await message.answer_video_note(video_note=roundvid)
    await message.answer(f'ID кружочка: {message.video_note.file_id}')
    
@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f'{message.from_user.first_name}, вам нужна помощь?')
    await message.answer(f'Ваш ID: {message.from_user.id}')
    
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