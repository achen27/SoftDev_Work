from pymongo import MongoClient

c = MongoClient()
db = c.test_database
restaurants = db.restaurants

f = open("primer-dataset.json","r")
rString = r.read()

rList = rString.split('\n')

for r in rList:
    restaurants.insert_one(r)
