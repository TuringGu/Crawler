from pyquery import PyQuery as pq

doc = pq(filename='demo2.html')
lis = doc('li').items()
print(type(lis))

for li in lis:
    print(li, type(li))