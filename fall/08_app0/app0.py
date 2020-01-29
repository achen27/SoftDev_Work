#Amber Chen
#SoftDev1 pd1
#K08 -- Lemme Flask You Sump’n
#2019-09-18

from flask import Flask
app = Flask(__name__)

@app.route("/")
def test0():
    print(__name__ + "1") #PRINTS IN TERMINAL
    return "No hablo quedefsefso!" #PRINTS ON WEBPAGE

@app.route("/test1") #ADD NAME TO END OF URL!!
def test1():
    print(__name__ + "2")
    return "this is the second route"

@app.route("/test2")
def test2():
    print(__name__ + "3")
    return "this is the third route"

if __name__ == "__main__": 
    app.debug = True
    app.run()
