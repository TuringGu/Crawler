import requests 

requests.get('http://httpbin.org/cookies/set/number/12333')
r1 = requests.get('http://httpbin.org/cookies')
print(r1.text)

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/12555')
r2 = s.get('http://httpbin.org/cookies')
print(r2.text)