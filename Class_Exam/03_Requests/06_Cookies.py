import requests

cookies = '_octo=GH1.1.2117198676.1574215521; _ga=GA1.2.1577169066.1574215525; _device_id=4fa2048e88c472422308cdba12fb9661'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,\
        image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

for cookies in cookies.split(';'):
    key, value = cookies.split('=', 1)
    jar.set(key, value)

r = requests.get('https://github.com/', cookies=jar, headers=headers)
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)
print(r.text)