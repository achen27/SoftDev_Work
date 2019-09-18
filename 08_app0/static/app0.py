from flask import Flask
app = Flask(__name__)

@app.route("/static")

def hello_world():
    print(__name__)
    return "No hablo quedefsefso!"

if __name__ == "__main__":
    app.debug = True
    app.run()
