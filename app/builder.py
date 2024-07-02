from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton


data = ("Nike", "Adidas", "Reebok")

inline_data = ("BMW", "Audi", "Mersedes")

def brands():
    keyboard = ReplyKeyboardBuilder()
    for brand in data:
        keyboard.add(KeyboardButton(text=brand))
    return keyboard.adjust(2).as_markup(resize_keyboard=True)

def inline_brands():
    inline_keyboard = InlineKeyboardBuilder()
    for inline_brand in inline_data:
        inline_keyboard.add(InlineKeyboardButton(text=inline_brand, callback_data=inline_brand))
    return inline_keyboard.adjust(2).as_markup()