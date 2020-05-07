import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq
 
async def main():
    # browser = await launch()
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://dynamic1.scrape.cuiqingcai.com/')
    await page.goto('https://dynamic2.scrape.cuiqingcai.com/')  

    await page.goBack()     # Go back
    await page.goForward()  # Go Forward
    await page.reload()     # Reload
    # await page.pdf()        # Save as pdf, Generating a pdf is currently only supported in Chrome headless
    await page.screenshot() # Screenshot
    await page.setContent('<h2>Hello World</h2>')   # Set page html
    await page.setUserAgent('Python')               # Set user agent
    await page.setExtraHTTPHeaders(headers={})      # Set header

    await page.close()      # Close
    await browser.close()   # Close

asyncio.get_event_loop().run_until_complete(main())
