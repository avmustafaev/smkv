import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.loadenv import envi

bot = Bot(token=envi.token)
dp = Dispatcher()

# Первая клавиатура
def get_first_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Нажми меня", callback_data="change_keyboard")]
    ])

# Вторая клавиатура
def get_second_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Я новая клавиатура", callback_data="new_keyboard")]
    ])

# Команда /start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Выбери действие:", reply_markup=get_first_keyboard())

# Обработчик нажатия на кнопку
@dp.callback_query(F.data == 'change_keyboard')
async def change_keyboard(callback: types.CallbackQuery):
    await callback.message.edit_text("Сообщение обновлено!", reply_markup=get_second_keyboard())

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())