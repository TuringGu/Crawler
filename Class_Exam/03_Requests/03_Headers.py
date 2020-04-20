import requests

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}

r = requests.get('https://static1.scrape.cuiqingcai.com/', headers=headers)
print(r.text)