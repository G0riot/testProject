from aiogram import Bot, Dispatcher, types, executor
from config import API_KEY
from keyboards import kb, ikb, endikb
from fetch_data import get_first_question, get_next, get_quiz


bot = Bot(API_KEY)
dp = Dispatcher(bot)
index = 1
quiz = get_quiz()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(text='Привіт! Чим займемося?')
    await message.bot.send_sticker(chat_id=message.chat.id,
                                   sticker='CAACAgIAAxkBAAEKGg5k5ihrBnw1wTg6LeP8RjvhS_yXfwACpRAAArRFoEpqI1qAWc6jRzAE',
                                   reply_markup=kb)


@dp.message_handler(commands=['quiz'])
async def start_quiz(message: types.Message):
    first_question = quiz[0]
    await message.reply(text=first_question, reply_markup=ikb)


@dp.callback_query_handler()
async def next_question(callback: types.CallbackQuery):
    global index
    if callback.data == 'next':
        question = await get_next(index)
        index += 1
        await callback.answer(text='Окей. Наступний пункт')
        await callback.message.reply(text=question, reply_markup=ikb)
    elif callback.data == 'cancel':
        await callback.message.answer(text='Привіт! Чим займемося?')
        await callback.message.bot.send_sticker(chat_id=callback.message.chat.id,
                                       sticker='CAACAgIAAxkBAAEKGg5k5ihrBnw1wTg6LeP8RjvhS_yXfwACpRAAArRFoEpqI1qAWc6jRzAE',
                                       reply_markup=kb)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
