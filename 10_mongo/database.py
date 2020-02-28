from pymongo import MongoClient
from bson.json_util import loads
import json

c = MongoClient("localhost",27017)
db = c.RAM
meteors = db.meteors

f = open("meteorites.json","r")
rString = f.read()
t = loads(rString)
# for i in t:
# 	print(i)
# 	print("\n")

meteors.insert_many(t)
