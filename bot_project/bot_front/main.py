from config import API_KEY
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboards import get_kb, get_cancel_kb
from fetch_data import get_quiz


storage = MemoryStorage()
bot = Bot(API_KEY)
dp = Dispatcher(bot, storage=storage)


question_list = {}


class ProfileStatesGroup(StatesGroup):
    name = State()
    surname = State()
    age = State()


@dp.message_handler(commands=['cancel'], state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    if state is None:
        return

    await state.finish()
    await message.reply('Ви скасували анкетування',
                        reply_markup=get_kb())


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Привіт! Давайте розпочнемо. ',
                         reply_markup=get_kb())


@dp.message_handler(commands=['create'])
async def cmd_create(message: types.Message) -> None:
    global question_list
    question_list = await get_quiz()
    my_question = question_list[0]
    await message.reply(text=my_question['text'],
                        reply_markup=get_cancel_kb())
    await ProfileStatesGroup.name.set()


@dp.message_handler(state=ProfileStatesGroup.name)
async def load_name(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['name'] = message.text
        my_question = question_list[1]
        await message.reply(text=my_question['text'])
        await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.surname)
async def load_name(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['surname'] = message.text
        my_question = question_list[2]
        await message.reply(text=my_question['text'])
        await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.age)
async def load_age(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['age'] = message.text

        await bot.send_photo(chat_id=message.from_user.id,
                             photo='https://img.freepik.com/premium-vector/facebook-like-icon-in-paper-cut-style_505135-238.jpg',
                             caption=f"{data['name']}, {data['surname']}\n Вік: {data['age']}")

        await message.answer('Анкетування завершено! Дякую!')
        await state.finish()


@dp.message_handler(lambda message: not message.text.isdigit() or float(message.text) > 100,
                    state=ProfileStatesGroup.age)
async def check_age(message: types.Message):
    await message.reply('Введіть реальний вік!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)