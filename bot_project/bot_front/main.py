import json

import aiohttp
from aiogram import Bot, Dispatcher, types, executor
from config import API_KEY, quiz_url
from keyboards import kb


bot = Bot(API_KEY)
dp = Dispatcher(bot)


@dp.message_handler(commands=['quiz'])
async def get_quiz(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=quiz_url) as response:
            if response.status == 200:
                quiz_list = await response.json()
                await message.answer(quiz_list)
            else:
                await message.answer("Server Error")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text, reply_markup=kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
