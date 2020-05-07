import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://www.taobao.com')
    await page.type('#q', 'Macbook pro')

    await asyncio.sleep(100)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
