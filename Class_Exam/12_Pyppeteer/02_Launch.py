import asyncio
from pyppeteer import launch

width, height = 1366, 768

async def main():
    # browser = await launch(devtools=True)   # Develop model, When devtools = True, headless will be closed

    # Headless model & UserData setting & Windows setting(infobars and windows size)
    browser = await launch(headless=False, userDataDir='./userdata', args=['--disable-infobars', f'--window-size={width},{height}']) 
   
    page = await browser.newPage()

    # Page size settings
    await page.setViewport({'width': width, 'height': height})

    # Webdriver detector bypass
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')

    # await page.goto('https://www.taobao.com')
    await page.goto('https://antispider1.scrape.cuiqingcai.com/')
    await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())