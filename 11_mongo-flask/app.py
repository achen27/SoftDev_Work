# Team Whatever (Amanda, Ivan)
# SoftDev pd1
# K11 -- Ay Mon Go Git It From Yer Flask
# 2020-03-08

from flask import Flask, render_template, request
from utl import mongogo

app = Flask(__name__)
mongogo.createDB()

@app.route('/')
def index():
    return render_template("_base.html")

@app.route('/results')
def results():
    mass = request.args.get('mass')
    print(request.form.keys())
    # print(mass)
    xcor = request.args.get('xcor')
    # print("xcor: "+xcor)
    ycor = request.args.get('ycor')
    # print("ycor: "+ycor)
    mclass = request.args.get('mclass')
    # print("class: "+mclass)
    year = request.args.get('year')
    # print("year: "+year)
    m = []
    if mass:
        m = filter_mass(int(mass))
    elif xcor and ycor:
        m = filter_coords(xcor,ycor)
    elif mclass:
        m = filter_class(mclass)
    elif year:
        m = filter_year(year)

    print(m)
    return render_template("results.html", meteors = m)

if __name__ == '__main__':
    app.debug = True
    app.run()
