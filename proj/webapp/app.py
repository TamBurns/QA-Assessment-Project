
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/c_search")
def c_search():
    return render_template("c_search.html")

@app.route("/s_search")
def s_search():
    return render_template("s_search.html")

@app.route("/newcard")
def newcard():
    return render_template("newcard.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


