from pymongo import MongoClient
import json

c = MongoClient()
db = c.test_database
restaurants = db.restaurants

f = open("primer-dataset.json","r")
rString = f.read()
print(rString)

rList = json.loads(rString)

#for r in rList:
print(rList[0])
restaurants.insert_one(rList[0])
