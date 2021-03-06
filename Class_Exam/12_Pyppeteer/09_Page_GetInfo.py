import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://dynamic2.scrape.cuiqingcai.com/')
    print('HTML:', await page.content())    # HTML info
    print('Cookies:', await page.cookies()) # Cookies info

    await asyncio.sleep(100)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
