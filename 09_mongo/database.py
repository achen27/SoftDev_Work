from pymongo import MongoClient
import json

c = MongoClient()
db = c.test_database
restaurants = db.restaurants

f = open("primer-dataset.json","r")
rString = f.read()

rList = rString.split('\n')

for r in rList:
    d = json.loads(r)
    restaurants.insert_one(d)
