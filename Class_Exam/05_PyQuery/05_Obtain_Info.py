from pyquery import PyQuery as pq

# Obtain Attribute Test1
doc = pq(filename='demo2.html')
a = doc('.item-0.active a')
print('\n\n')
print(a, '\n', type(a))
print(a.attr('href'))   # Obtain Attribute
print(a.attr.href)  # Obtain Attribute


# Obtain Attribute Test2
a2 = doc('a')
print('\n\n')
print(a2, '\n', type(a2))
print(a2.attr('href'))  # Only Get one

# Get All
print('\n')
for item in a2.items():
    print(item.attr('href'))


# Obtain Text Test1
a3 = doc('.item-0.active a')
print('\n\n', a3)
print(a.text())
print(a3.html())


# Obtain Text Test2
a4 = doc('li')
print('\n\n', a4.html())
print(a4.text())
print(type(a4.text()))