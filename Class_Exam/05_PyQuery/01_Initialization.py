from pyquery import PyQuery as pq
import requests

html = '''
<div>
    <ul>
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''

# String Initialize
print('\n\nString Initialize:')
doc1 = pq(html)
print(doc1('li'))

# URL Initialize
print('\n\nURL Initialize:')
doc21 = pq(url='https://turinggu.github.io')
print(doc21('title'))
doc22 = pq(requests.get('https://turinggu.github.io').text)
print(doc22('title'))

# File Initialize
print('\n\nFile Initialize:')
doc3 = pq(filename='demo.html')
print(doc3('li'))



