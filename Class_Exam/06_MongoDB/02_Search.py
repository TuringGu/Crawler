import pymongo
from bson.objectid import ObjectId

# Connect
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

# Searching by name
result1 = collection.find_one({'name': 'John'})
print('\n\nResult1:')
print(type(result1))
print(result1)


# Searching by ObjectId
result2 = collection.find_one({'_id': ObjectId('5ea1a3ee608251a8fec15910')})
print('\n\nResult2:')
print(result2)


# Searching multiple data
results3 = collection.find({'age': 20})
print('\n\nResult3:')
print(results3)
for result3 in results3:
    print(result3)


# Searching by conditions
# results4 = collection.find({'age': {'$gt': 20}})
results4 = collection.find({'name': {'$regex': '^J.*'}})
print('\n\nResult4:')
print(results4)
for result4 in results4:
    print(result4)