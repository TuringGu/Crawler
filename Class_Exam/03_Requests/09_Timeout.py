import requests

# r = requests.get('http://httpbin.org/get', timeout=1)
# r = requests.get('http://httpbin.org/get', timeout=None)
r = requests.get('http://httpbin.org/get', timeout=(5, 30))    # (connect, read)
print(r.status_code)