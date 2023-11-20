from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton(text='/start')
b2 = KeyboardButton(text='/help')
b3 = KeyboardButton(text='/quiz')

kb.add(b1, b2, b3)

ikb = InlineKeyboardMarkup()
ib1 = InlineKeyboardButton(text='Next', callback_data='next')
ib2 = InlineKeyboardButton(text='Cancel', callback_data='cancel')

ikb.add(ib1, ib2)


endikb = InlineKeyboardMarkup(InlineKeyboardButton(text="End"))
