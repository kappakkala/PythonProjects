from pymongo import MongoClient

client = MongoClient("localhost", 27017)

# prints all the available databases
# print(client.list_database_names())

# prints the available collections inside a db
# print(db.list_collection_names())

# create a new database name person
db = client["person"]
# create a collection associated with the database
collection = db["hobby"]
# attach a single document
data = {"name": "swimming", "years": 2, "active": False}
# document = collection.insert_one(data)

# attach multiple documents
data = [
    {"name": "badminton", "years": 4, "active": True},
    {"name": "gaming", "years": 1, "active": True},
    {"name": "films", "years": 10, "active": True},
    {"name": "coins", "years": 20, "active": False},
]
document = collection.insert_many(data)

# for document in collection.find():
#    print(document)

# count the total documents inside a collection
stats = db.command("dbstats")
print(stats)
# data = {"name": "swimming", "years": 2, "active": False}
# collection.delete_one(data)

# for document in collection.find():
#    print(document)

# drops a collection from db
# check = db.drop_collection(collection)
# the ok field in check returns either 1 or 0
# if bool(check['ok']):
#    print("Collection deleted from db")
# else:
#     print("Collection not found in db")

# deletes a database
# print(client.drop_database('person'))
