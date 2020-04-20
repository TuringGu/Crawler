# Have error: TypeError: a bytes-like object is required, not 'str'
from requests import Request, Session

url = 'http://httpbin.org/post'
data = {'name', 'TuringGu'}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
# prepped = req.prepare()
prepped = s.prepare_request(req)
r = s.send(prepped)
# r = s.send(prepped.encode('utf-8'))
print(r.text)