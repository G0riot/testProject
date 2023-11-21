from config import API_KEY
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboards import get_kb, get_cancel_kb
from fetch_data import get_quiz
from db_sqlite import db_start, create_profile, edit_profile


async def on_startup(_):
    await db_start()


storage = MemoryStorage()
bot = Bot(API_KEY)
dp = Dispatcher(bot, storage=storage)


class ProfileStatesGroup(StatesGroup):
    name = State()
    surname = State()
    age = State()
    photo = State()


@dp.message_handler(commands=['cancel'], state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    if state is None:
        return

    await state.finish()
    await message.reply('Ви скасували анкетування',
                        reply_markup=get_kb())


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Привіт! Давайте розпочнемо.',
                         reply_markup=get_kb())


@dp.message_handler(commands=['create'])
async def cmd_create(message: types.Message) -> None:
    global question_list
    question_list = await get_quiz()
    my_question = question_list[0]
    await message.reply(text=my_question['text'],
                        reply_markup=get_cancel_kb())
    await ProfileStatesGroup.name.set()
    await create_profile(user_id=message.from_user.id)


@dp.message_handler(state=ProfileStatesGroup.name)
async def load_name(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['name'] = message.text
        my_question = question_list[1]
        await message.reply(text=my_question['text'])
        await ProfileStatesGroup.surname.set()


@dp.message_handler(state=ProfileStatesGroup.surname)
async def load_name(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['surname'] = message.text
        my_question = question_list[2]
        await message.reply(text=my_question['text'])
        await ProfileStatesGroup.age.set()


@dp.message_handler(state=ProfileStatesGroup.age)
async def load_age(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['age'] = message.text
        my_question = question_list[3]
        await message.reply(text=my_question['text'])
        await ProfileStatesGroup.photo.set()


@dp.message_handler(content_types=['photo'], state=ProfileStatesGroup.photo)
async def load_photo(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=f"{data['name']} {data['surname']}\nВік: {data['age']}")

        await edit_profile(data, user_id=message.from_user.id)
        await message.answer('Анкетування завершено! Дякую!')
        await state.finish()



@dp.message_handler(lambda message: not message.text.isdigit() or float(message.text) > 100,
                    state=ProfileStatesGroup.age)
async def check_age(message: types.Message):
    await message.reply('Введіть реальний вік!')


@dp.message_handler(lambda message: not message.photo, state=ProfileStatesGroup.photo)
async def check_photo(message: types.Message):
    await message.reply('Введена інформація це не фото!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
