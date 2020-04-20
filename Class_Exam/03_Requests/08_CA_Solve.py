import requests
from requests.packages import urllib3

# Ignore warnings
urllib3.disable_warnings()

# verify=False: Do not verify CA
response = requests.get('https://static2.scrape.cuiqingcai.com/', verify=False)
print(response.status_code)