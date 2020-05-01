import asyncio
import requests
import time

start = time.time() # Start Time

async def get(url):
    return requests.get(url)

async def request():
    # url = 'https://static4.scrape.cuiqingcai.com/'    # HSTS Error
    url = 'https://blog.51cto.com/'
    print('Waiting for', url)

    # response = requests.get(url)    # Bad Example
    # Need to have await operation, but await can't be used with requests
    # response = await requests.get(url)  
    response = await get(url)
    
    print('Get response from', url, 'response', response)



tasks = [asyncio.ensure_future(request()) for _ in range(5)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()   # End Time
print('Cost time:', end - start)
