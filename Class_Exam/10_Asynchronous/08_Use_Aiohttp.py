import asyncio
import aiohttp
import time

def test(number):
    start = time.time() # Start time

    async def get(url):
        session = aiohttp.ClientSession()
        response = await session.get(url)
        await response.text()
        await session.close()
        return response

    async def request():
        url = 'https://www.baidu.com/'
        # print('Waiting for', url)
        # response = await get(url)
        # print('Get response from', url, 'response', response)
        await get(url)

    tasks = [asyncio.ensure_future(request()) for _ in range(number)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    end = time.time()   # End Time
    print('Number:', number , 'Cost time:', end - start)


for number in [1, 3, 5, 10, 15, 30, 50, 75, 100, 200, 500]:
    test(number)