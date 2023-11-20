import aiohttp
from config import quiz_url


async def get_quiz():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=quiz_url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return f'Error! Code: {response.status}'


async def get_first_question():
    quiz_list = await quiz
    first_question = quiz_list[0]
    return first_question['text']


async def get_next(index):
    quiz_list = await get_quiz()
    text = ''
    if len(quiz_list) > index:
        question = quiz_list[index]
        if len(quiz_list) - 1 == index:
            text = 'Це останнє запитання! '
        return text + question['text']
    else:
        return f'Error!'
