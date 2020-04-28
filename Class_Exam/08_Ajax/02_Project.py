import requests
import logging
import json
from os import makedirs
from os.path import exists

LIMIT = 10  # Page list limit
TOTAL_PAGE = 10 # Scrape page number
RESULTS_DIR = 'results' # Dir to store files
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

INDEX_URL = 'https://dynamic1.scrape.cuiqingcai.com/api/movie/?limit={limit}&offset={offset}'
DETAIL_URL = 'https://dynamic1.scrape.cuiqingcai.com/api/movie/{id}'
####################################################


# Scrape html code from url page
# Input: (String) URL
# Output: (String) Response of json String
def scrape_api(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)
####################################################


# Scrape html code from index page
# Input: (Int) Index of page
# Output: (String) Response of json String
def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)
####################################################


# Scrape info from detail page
# Input: (Int) Id of detail page
# Output: (String) Response of json String
def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)
####################################################


# Save data to file
# Input: (String) Json data
# Output: (file) file
def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
####################################################


# Main 
def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_data = scrape_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail data %s', detail_data)
            save_data(detail_data)

if __name__ == '__main__':
    main()
