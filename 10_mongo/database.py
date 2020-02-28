from pymongo import MongoClient
from bson.json_util import loads
import json

c = MongoClient()
db = c.RAM
meteors = db.meteors

f = open("meteorites.json","r")
rString = f.readlines()
t = loads(rString)
