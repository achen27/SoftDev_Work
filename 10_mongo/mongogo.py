from pymongo import MongoClient
from bson.json_util import loads
from pprint import pprint

c = MongoClient()
db = c.RAM
meteors = db.meteors

if (meteors in db.list_collection_names()):
    f = open("meteorites.json","r")
    rString = f.readlines()
    t = loads(rString)
