import asyncio
import aiohttp
import logging
import json
from motor.motor_asyncio import AsyncIOMotorClient

# Mongodb initialize
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'books'
MONGO_COLLECTION_NAME = 'books20200505'
client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

# Scrape initialize
PAGE_SIZE = 18
PAGE_NUMBER = 10
CONCURRENCY = 5
ids = []
INDEX_URL = 'https://dynamic5.scrape.cuiqingcai.com/api/book/?limit=18&offset={offset}'
DETAIL_URL = 'https://dynamic5.scrape.cuiqingcai.com/api/book/{id}'
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
semaphore = asyncio.Semaphore(CONCURRENCY)
session = None


# Scrape page by url
async def scrape_api(url):
    async with semaphore:
        try:
            logging.info('scraping %s', url)
            async with session.get(url) as response:
                return await response.json()

        except aiohttp.ClientError:
            logging.error('error occurred while scraping %s', url, exc_info=True)

# Scrape index of the detail page
async def scrape_index(page):
    url = INDEX_URL.format(offset=PAGE_SIZE * (page - 1))
    return await scrape_api(url)

# Store data to mongodb
async def save_data(data):
    logging.info('saving data %s', data)
    if data:
        return await collection.update_one({'id': data.get('id')}, {'$set': data}, upsert = True)

# Scrape detail page info
async def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    data = await scrape_api(url)
    await save_data(data)


# Main
async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, PAGE_NUMBER + 1)]
    results = await asyncio.gather(*scrape_index_tasks)
    logging.info('results %s', json.dumps(results, ensure_ascii=False, indent=2))

    # Scrape Book ID from the results
    for index_data in results:
        if not index_data: continue
        for item in index_data.get('results'):
            ids.append(item.get('id'))

    # Scrape detail page info
    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in ids]
    await asyncio.wait(scrape_detail_tasks)
    await session.close()


# Run
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())