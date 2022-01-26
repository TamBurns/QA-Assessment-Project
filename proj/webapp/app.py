
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_HOST'] = 'panda_db'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL()
mysql.init_app(app)


@app.route("/")
def home():
    cursor = mysql.connection.cursor()

    cursor.execute(f"use panda_db;")
    cursor.execute(f"SELECT * FROM 'cocktails';")
    count = cursor.fetchall()
    cursor.close()

    return render_template("home.html", count = count)

@app.route("/c_search")
def c_search():
    return render_template("c_search.html")

@app.route("/s_search")
def s_search():
    return render_template("s_search.html")

@app.route("/newcard")
def newcard():
    return render_template("newcard.html")

@app.route("/help")
def help():
    return render_template("help.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


