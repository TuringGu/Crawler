import requests
import socks
import socket


# Proxies
proxy = '127.0.0.1:1080'
proxy = 'username:password@127.0.0.1:1080'

# HTTP proxy
proxies_http = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}

# Socks5 proxy method 1
proxies_socks5_01 = {
    'http': 'socks5://' + proxy,
    'https': 'socks5://' + proxy
}

# Socks5 proxy method 2
socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 1080)
socket.socket = socks.socksocket


try:
    # response = requests.get('https://httpbin.org/get', proxies=proxies_http)
    response = requests.get('https://httpbin.org/get')  # Socks5 proxy method 2
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)