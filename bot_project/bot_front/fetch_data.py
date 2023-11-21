import aiohttp
from config import quiz_url


async def get_quiz():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=quiz_url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return f'Error! Code: {response.status}'