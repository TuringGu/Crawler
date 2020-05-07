import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://turinggu.github.io/')
    await page.waitForSelector('.post-footer .button')

    await page.click('.post-footer .button', options={
        'button': 'left',  # left, middle, right
        'clickCount': 1,    # 1, 2, etc...
        'delay': 3000,      # Millisecond
    })

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
