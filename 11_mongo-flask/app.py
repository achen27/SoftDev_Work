# Team Whatever (Amanda, Ivan)
# SoftDev pd1
# K11 -- Ay Mon Go Git It From Yer Flask
# 2020-03-08

from flask import Flask, render_template
from utl import mongogo

app = Flask(__name__)
mongogo.createDB()

@app.route('/')
def index():
    return render_template("_base.html")

@app.route('/results')
def results():
    mass = request.args.get('mass')
    xcor = request.args.get('xcor')
    ycor = request.args.get('ycor')
    mclass = request.args.get('mclass')
    year = request.args.get('year')
    ß
    return render_template("list.html", meteors = m)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
