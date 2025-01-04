import asyncio
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from app.loadenv import envi
from aiogram.enums import ChatAction
import app.keyboards as kb
import app.builder as builder


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    # await message.reply('Привет!')
    await message.answer('Как дела?')
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(0.5)
    await message.answer_photo(photo=envi.kn1pic_id, caption='Вы присоединились к боту отчётов KN1')
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.RECORD_VIDEO_NOTE)
    await asyncio.sleep(0.5)
    await message.answer_video_note(video_note=envi.video_note_hello, reply_markup=kb.main)
    
@router.message(F.text =='привет!')
async def echo(message: Message):
    await message.answer('ну и тебе тоже')
    
@router.message(F.photo)
async def get_photo(message: Message):
    photo_id = message.photo[-1].file_id
    await message.answer_photo(photo=photo_id)
    await message.answer(f'ID фотографии: {message.photo[-1].file_id}')
    
@router.message(F.contact)
async def get_photo(message: Message):
    phone_num = message.contact.phone_number
    # await message.answer_contact(phone_number=phone_num,first_name=message.contact.first_name)
    await message.answer(f'Ваш номер телефона: {phone_num}', reply_markup=kb.inline_main)
    
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
    
    
@router.callback_query(F.data == 'basket')
async def basket(callback: CallbackQuery):
    await callback.answer('КОрзина')
    await callback.message.answer('Ваша корзина пуста.', reply_markup=builder.inline_brands())
    
@router.callback_query(F.data == 'catalog')
async def basket(callback: CallbackQuery):
    await callback.answer('Каталог')
    await callback.message.answer('Ваш каталог:', reply_markup=builder.brands ())

    
@router.message()
async def echo(message: Message):
    await message.answer('Это неизвестная команда.')