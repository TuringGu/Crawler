import asyncio
from pyppeteer import launch

width, height = 1366, 768

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://turinggu.github.io/')
    await page.waitForSelector('.post-footer .button')   # Delay waiting
    await asyncio.sleep(2)
    await page.screenshot(path='example20200507.png')
    
    # JS execute, return the page info
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')

    print(dimensions)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
