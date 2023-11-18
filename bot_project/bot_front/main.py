from aiogram import Bot, Dispatcher, types, executor
from config import API_KEY
from keyboards import kb
from aiohttp import request


bot = Bot(API_KEY)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text, reply_markup=kb)


@dp.message_handler(commands=['/quiz'])
async def get_quiz():
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
