import asyncio
import aiohttp

proxy = 'http://127.0.0.1:1080'


# Error: Only http proxies are supported
# While aiohttp supports proxies that upgrade to HTTPS via CONNECT, it doesn't support proxies that must be connected to via `https://`
# https://github.com/aio-libs/aiohttp/pull/4110

async def main():
    async with aiohttp.ClientSession() as session:
        # async with session.get('https://httpbin.org/get', proxy=proxy) as response:   # Error one
        async with session.get('http://httpbin.org/get', proxy=proxy) as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
