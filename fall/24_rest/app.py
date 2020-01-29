# Amanda Chen
# SoftDev1 pd1
# K24 -- A RESTful Journey Skyward
# 2019-11-12

from flask import Flask, render_template, request, redirect, url_for
import json
from urllib.request import urlopen
app = Flask(__name__)

#API_KEY: ADkAYcwkCPEKYm7EHBmjKuc9D8Dd4GmC8i30vDpe


@app.route("/")
def root():
    print(app)
    u = urlopen("https://api.nasa.gov/planetary/apod?api_key=ADkAYcwkCPEKYm7EHBmjKuc9D8Dd4GmC8i30vDpe")
    response = u.read();
    data = json.loads(response);
    return render_template('root.html',
                            pic = data['url'],
                            date = data['date'],
                            caption = data['explanation'])


if __name__ == "__main__":
    app.debug = True
    app.run()
