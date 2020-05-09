import asyncio
from pyppeteer import launch

proxy = '127.0.0.1:1080'

async def main():
    # browser = await launch({'args': ['--proxy-server=http://' + proxy], 'headless': False})
    browser = await launch({'args': ['--proxy-server=socks5://' + proxy], 'headless': False})
    page = await browser.newPage()
    await page.goto('https://httpbin.org/get')
    print(await page.content())
    await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())