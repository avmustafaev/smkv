from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')],
    [KeyboardButton(text='Отправить локацию', request_location=True), KeyboardButton(text='Отправить контакт', request_contact=True)]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')