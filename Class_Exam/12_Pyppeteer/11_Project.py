import logging
import asyncio
import json
from pyppeteer import launch
from pyppeteer.errors import TimeoutError
from os import makedirs
from os.path import exists


TIMEOUT = 10
TOTAL_PAGE = 10
HEADLESS = False
RESULTS_DIR = 'results20200508'
WINDOW_WIDTH, WINDOW_HEIGHT = 1366, 768
INDEX_URL = 'https://dynamic2.scrape.cuiqingcai.com/page/{page}'
browser, tab = None, None

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)


# Browser initialize
async def init():
    global browser, tab
    # Note: in --windows-size, the parameter should not have blank space
    browser = await launch(headless=HEADLESS, args=['--disable-infobars', f'--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}'])
    tab = await browser.newPage()
    await tab.setViewport({'width': WINDOW_WIDTH, 'height': WINDOW_HEIGHT})


# Scrape page info by url & selector
async def scrape_page(url, selector):
    logging.info('scraping %s', url)
    try:
        await tab.goto(url)
        await tab.waitForSelector(selector, options={'timeout': TIMEOUT * 1000})
    except TimeoutError:
        logging.error('error occurred while scraping %s', url, exc_info=True)


# Scrape index of page
async def scrape_index(page):
    url = INDEX_URL.format(page=page)
    await scrape_page(url, '.item .name')


# Get info from pages
async def parse_index():
    return await tab.querySelectorAllEval('.item .name', 'nodes => nodes.map(node => node.href)')


# Scrape detail page by url
async def scrape_detail(url):
    await scrape_page(url, 'h2')


# Scrape detail info from detail page
async def parse_detail():
    url = tab.url
    name = await tab.querySelectorEval('h2', 'node => node.innerText')
    categories = await tab.querySelectorAllEval('.categories button span', 'nodes => nodes.map(node => node.innerText)')
    cover = await tab.querySelectorEval('.cover', 'node => node.src')
    score = await tab.querySelectorEval('.score', 'node => node.innerText')
    drama = await tab.querySelectorEval('.drama p', 'node => node.innerText')
    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }


# Save data
async def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


# Main
async def main():
    await init()
    try:
        for page in range(1, TOTAL_PAGE + 1):
            await scrape_index(page)
            detail_urls = await parse_index()
            for detail_url in detail_urls:
                await scrape_detail(detail_url)
                detail_data = await parse_detail()
                logging.info('data %s', detail_data)
                await save_data(detail_data)
    finally:
        await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())