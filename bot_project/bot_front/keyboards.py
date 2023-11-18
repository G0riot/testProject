from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/start')
b2 = KeyboardButton(text='/help')
b3 = KeyboardButton(text='/quiz')

kb.add(b1, b2, b3)
