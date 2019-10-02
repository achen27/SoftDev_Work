from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


name = "Team Egg Fried Rice Period 1"
roster = "Amanda Chen & Tiffany Cao"
correctU = "Eggs"
correctP = "friedrice"

@app.route("/")

def root():
    print(app)
    return render_template('login.html',
                            team = name,
                            rost = roster)

@app.route("/auth")
def authenticate():
    if (request.args('username') == correctU and request.cookies.get('password') == correctP) :
       return redirect ("/")
    else: return redirect ("/error")


@app.route("/error")
def err():
    return "blaaa"


if __name__ == "__main__":
    app.debug = True
    app.run()
