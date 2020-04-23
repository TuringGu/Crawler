from pyquery import PyQuery as pq

# addClass & removeClass Test1
doc = pq(filename='demo2.html')
li = doc('.item-0.active')
print(li)
li.remove_class('active')
# li.removeClass('active')
print(li)
li.add_class('active')
print(li)



# attr, text, html Test2
html2 = '''
    <ul class="list">
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
    </ul>
'''

doc2 = pq(html2)
print('\n\n')
li2 = doc2('.item-0.active')
print(li2)
li2.attr('name', 'link')
print(li2)
li2.text('change item')
print(li2)
li2.html('<span>changed item</span>')
print(li2)


# remove Test3
html3 = '''
    <div class="wrap">
        Hello, World
        <p>This is a paragraph.</p>
    </div>
'''

doc3 = pq(html3)
wrap = doc3('.wrap')
print('\n\n')
print(wrap.text())

print('\n\n')
wrap.find('p').remove()
print(wrap.text())