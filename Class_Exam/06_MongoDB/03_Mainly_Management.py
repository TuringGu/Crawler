import pymongo
from bson.objectid import ObjectId

# Connect
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students



# Count
count1 = collection.find().count()
print(count1)
count2 = collection.find({'age': 20}).count()
print(count2)



# Sort
results = collection.find().sort('name', pymongo.ASCENDING) # DECENDING
print([result['name'] for result in results])



# Offset
results1 = collection.find().sort('name', pymongo.ASCENDING).skip(2)
results2 = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results1])
print([result['name'] for result in results2])

# Don't use big offset to avoid out of memory
results3 = collection.find({'_id': {'$gt': ObjectId('5ea1a3ee608251a8fec15900')}})
print([result['_id'] for result in results3])



# Update
condition = {'name': 'John'}
student = collection.find_one(condition)
student['age'] = 26
# result41 = collection.update(condition, student)
result42 = collection.update(condition, {'$set': student})
print(result42)

# update_one & update_many test4
condition = {'name': 'John'}
student = collection.find_one(condition)
student['age'] = 28
result43 = collection.update_one(condition, {'$set': student})
print(result43)
print(result43.matched_count, result43.modified_count)

# update_one & update_many test5
condition = {'age': {'$gt': 18}}
# result5 = collection.update_one(condition, {'$inc': {'age': 1}})
result5 = collection.update_many(condition, {'$inc': {'age': 1}})
print(result5)
print(result5.matched_count, result5.modified_count)



# Delete
# result61 = collection.remove({'name': 'Kevin'})
# print(result61)
result62 = collection.delete_one({'name': 'John'})
print(result62.deleted_count)
result63 = collection.delete_many({'age': {'$lt': 20}})
print(result63.deleted_count)