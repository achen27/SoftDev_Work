# Amanda Chen
# SoftDev1 pd1
# K25 -- Getting More REST
# 2019-11-13

from flask import Flask, render_template, request, redirect, url_for
import json
from urllib.request import urlopen
app = Flask(__name__)


@app.route("/")
def root():
    return render_template('root.html')

#Dark Sky API
#API_KEY: 1975880ad720859dec79321ed72598c5
#https://api.darksky.net/forecast/[key]/[latitude],[longitude]
@app.route("/weather")
def weather():
    print(app)
    u = urlopen("https://api.darksky.net/forecast/1975880ad720859dec79321ed72598c5/40.713051,-74.007233")
    response = u.read();
    info = json.loads(response);
    #print(info['daily']['data'][0])
    return render_template('weather.html',
                            lat = info['latitude'],
                            long = info['longitude'],
                            timezone = info['timezone'],
                            sum = info['daily']['summary'],
                            high = info['daily']['data'][0]['temperatureHigh'],
                            low = info['daily']['data'][0]['temperatureLow'])

#Rest Countries API
#No API Key
#https://restcountries.eu/rest/v2/
@app.route("/country")
def country():
    print(app)
    u = urlopen("https://restcountries.eu/rest/v2/name/France")
    response = u.read();
    info = json.loads(response);
    #print(info['daily']['data'][0])
    return render_template('country.html',
                            name = info[0]['name'],
                            pop = info[0]['population'],
                            cap = info[0]['capital'],
                            cur = info[0]['currencies'][0]['name'],
                            reg = info[0]['subregion'],
                            area = info[0]['area'])

#Unsplash
#API_KEY: ae7faf91895099838aac4db456686b8c4dfc427579a7f9c88eaed9e6d3f04c59
#https://api.unsplash.com/photos/random?client_id=ae7faf91895099838aac4db456686b8c4dfc427579a7f9c88eaed9e6d3f04c59
@app.route("/photo")
def photo():
    print(app)
    u = urlopen("https://api.unsplash.com/photos/random?client_id=ae7faf91895099838aac4db456686b8c4dfc427579a7f9c88eaed9e6d3f04c59")
    response = u.read();
    info = json.loads(response);
    #print(info['daily']['data'][0])
    return render_template('photo.html',
                            photo = info['urls']['small'],
                            date = info['created_at'][:10],
                            descrip = info['alt_description'].title(),
                            name = info['user']['name'])


if __name__ == "__main__":
    app.debug = True
    app.run()
