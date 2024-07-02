import asyncio
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from app.loadenv import envi
from aiogram.enums import ChatAction
import app.keyboards as kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    # await message.reply('Привет!')
    await message.answer('Как дела?', reply_markup=kb.main)
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(2)
    await message.answer_photo(photo=envi.kn1pic_id, caption='Вы присоединились к боту отчётов KN1')
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.RECORD_VIDEO_NOTE)
    await asyncio.sleep(2)
    await message.answer_video_note(video_note=envi.video_note_hello)
    
@router.message(F.text =='привет!')
async def echo(message: Message):
    await message.answer('ну и тебе тоже')
    
@router.message(F.photo)
async def get_photo(message: Message):
    photo_id = message.photo[-1].file_id
    await message.answer_photo(photo=photo_id)
    await message.answer(f'ID фотографии: {message.photo[-1].file_id}')
    
@router.message(F.video_note)
async def get_round(message: Message):
    roundvid = message.video_note.file_id
    await message.answer_video_note(video_note=roundvid)
    await message.answer(f'ID кружочка: {message.video_note.file_id}')
    
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        f"{f'{message.from_user.last_name} {message.from_user.first_name}'}, вам нужна помощь?"
    )
    await message.answer(f'Ваш ID: {message.from_user.id}')
    
@router.message()
async def echo(message: Message):
    await message.answer('Это неизвестная команда.')