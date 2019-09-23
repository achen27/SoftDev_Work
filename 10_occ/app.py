#Amber Chen & Vishwa Sofat
#SoftDev1 pd1
#K10 -- NO-body expects the Spanish Inquisition!
#2019-09-11

import random

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return ("Welcome")

@app.route("/occupyflaskst")
def occupier():
    return render_template('occupyflaskst.html',
        tab = "Occupations Table",
        titulo = "Occupations",
        team = "Team Silencio Pd1")

if __name__ == "__main__":
    app.debug = True
    app.run()

#opening file
f = open("occupations.csv","r")

#storing file into large string
fString = f.read()

#spliting string into array with name and percentage as an element
fList = fString.split('\n')

#creating new array with each element as an array with name and percentage
fNewList = []
for s in fList:
    fNewList.append(s.rsplit(',',1))

def randomOcc():
    r = random.randint(1, 998) / 10.0
    #print("random num: " + str(r))
    for o in fNewList[1:-2]:
        r -= float(o[1])
        if (r <= 0):
            return o[0]
