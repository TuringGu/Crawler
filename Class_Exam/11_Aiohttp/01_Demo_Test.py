import aiohttp
import asyncio

async def fetch(session, url):
    # Context manager
    async with session.get(url) as response:
        # If returned object is a coroutine, it need to add await ahead
        return await response.text(), response.status

async def main():
    # Context manager
    async with aiohttp.ClientSession() as session:
        html, status = await fetch(session, 'https://turinggu.github.io')
        print(f'html: {html[:100]}...') # Only print head 100 charactors
        print(f'status: {status}')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main()) #  Explicitly Declared  
    # asyncio.run(main())   # Implicitly declared, (After python 3.7 )  