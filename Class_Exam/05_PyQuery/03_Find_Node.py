from pyquery import PyQuery as pq

doc = pq(filename='demo2.html')
items = doc('.list')
print(type(items))
print(items)


# Find children node
# lis = items.find('li')
# lis = items.children()    # Only find children node
lis = items.children('.active')
print(type(lis))
print(lis)


# Find father node
doc2 = pq(filename='demo2.html')
items2 = doc2('.list')
container = items.parent()  # Only find direct father node
print(type(container))
print(container)
print('\n\n')
# parents = items.parents()   # Find all the parents node
parents = items.parents('.wrap')    # Find a specified parents node
print(type(parents))
print(parents)


# Find brother node
doc3 = pq(filename='demo2.html')
li = doc3('.list .item-0.active')
print('\n\n')
print(li.siblings)
