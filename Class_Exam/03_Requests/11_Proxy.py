import requests

proxies1 = {
    'http': 'http://127.0.0.1:1080',
    'https': 'https://127.0.0.1:1080'
}

proxies2 = {
    'http': 'http://user:password@127.0.0.1:1080/',
    'https': 'https://user:password@127.0.0.1:1080/'
}

proxies3 = {
    'http': 'socks5://user:password@host:port',
    'https': 'socks5://user:password@host:port'
}


r1 = requests.get('https://httpbin.org/get', proxies=proxies1)
print(r1.text)