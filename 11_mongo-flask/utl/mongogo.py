from pymongo import MongoClient
from bson.json_util import loads

client = MongoClient()
db = client.RAM
collection = db.meteors


def createDB():
    client.drop_database('RAM')
    file = open("doc/meteorites.json","r")
    data = file.read()
    meteors = loads(data)
    collection.insert_many(meteors)
    file.close()
    client.close()

# Dataset: Earth Meteorite Landings
# Collection of data of 1000 meteors that landed on Earth by NASA
# Includes their name, class, date fell, and coordinates where it fell
# Link: https://data.nasa.gov/resource/y77d-th95.json
# We imported that dataset onto mongo by reading the json into a string and loading it into mongo.
# Before loading we cleaned the dataset be removing the last two extra columns for some rows
# ,":@computed_region_cbhk_fwbd":"[0-9]{1,}",":@computed_region_nnqa_25f4":"[0-9]{1,}"

def filter_mass(mass):
    return list(meteors.find({'mass':mass}))

def filter_coords(longitude, lat):
    return list(meteors.find({'reclong':longitude, 'reclat': lat}))

def filter_class(recclass):
    return list(meteors.find({'recclass':recclass}))

def filter_year(year):
    return list(meteors.find({'year':year}))
