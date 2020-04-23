import pymongo

# Connect
client = pymongo.MongoClient(host='localhost', port=27017)
# client = pymongo.MongoClient('mongodb://localhost:27017')


# Select DB
db = client.test
# db = client['test']


# Specifying collection
collection = db.students
# collection = db['students']


# Insert data
student1 = {
    'id': '20170104',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170105',
    'name': 'John',
    'age': 22,
    'gender': 'female'
}

# result = collection.insert_one(student1) # Attention: not Insert
# print(result)
# print(result.inserted_id)
result = collection.insert_many([student1, student2])
print(result)
print(result.inserted_ids)

