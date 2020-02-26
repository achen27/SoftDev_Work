from pymongo import MongoClient
import json

c = MongoClient()
db = c.test_database
restaurants = db.restaurants

f = open("primer-dataset.json","r")
rString = f.read()

rList = json.loads(rString)

for r in rList:
    # print(r)
    restaurants.insert_one(r)
