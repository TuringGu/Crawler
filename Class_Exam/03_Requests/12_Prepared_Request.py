from requests import Request, Session

url = 'http://httpbin.org/post'

# Debug: 
# 1. tranlate to byte to solve this problem
# 2. Restart the environment
# TypeError: a bytes-like object is required, not 'str'
data = {'name': 'TuringGu'}   

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
resp = s.send(prepped)
print(resp.text)