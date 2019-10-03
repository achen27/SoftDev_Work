# Amanda Chen
# SoftDev1 pd1
# K15 -- Do I Know You?
# 2019-10-02

from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)


name = "Team Egg Fried Rice Period 1"
roster = "Amanda Chen & Tiffany Cao"
username = "Eggs"
password = "friedrice"

app.secret_key = "abcd"

@app.route("/")

def login():
    print(app)
    if 'user' in session:
         return redirect (url_for("welcome"))
    else:
        return render_template('login.html',
                                team = name,
                                rost = roster)

@app.route("/welcome")
def welcome():
    print(app)
    return render_template('welcome.html',
                            team = name,
                            rost = roster,
                            name = session['user'])

@app.route("/logout")
def logout():
    print(app)
    session.pop('user')
    return render_template('logout.html',
                            team = name,
                            rost = roster)

@app.route("/auth")
def authenticate():
    print(url_for("login"))
    session['user'] = request.args['username']
    session['pass'] = request.args['password']
    print(session['user'])
    print(session['pass'])
    if (request.args['username'] == username and request.args['password'] == password) :
       return redirect (url_for("login"))
    else:
        return redirect (url_for("err"))


@app.route("/error")
def err():
    print(request.form)
    r = ''
    if (session['user'] != username):
        r = "Username does not exist. Try again."
    else:
        r = "Password does not match Username. Try again."
    session.pop('user')
    return render_template('error.html',
                            team = name,
                            rost = roster,
                            reason = r)


if __name__ == "__main__":
    app.debug = True
    app.run()
