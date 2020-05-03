import aiohttp
import asyncio

async def main():
    data = {'name': 'TuringGu', 'age': 18}
    async with aiohttp.ClientSession() as session:
        # async with session.post('https://httpbin.org/post', data=data) as response:
        #     print(await response.text())
        
        # Post Json data
        async with session.post('https://httpbin.org/post', json=data) as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
    