from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_HOST'] = 'panda_db'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL()
mysql.init_app(app)

cursor = mysql.connection.cursor()
cursor.execute(f"use panda_db;")
cursor.execute(f"SELECT * FROM 'cocktails';")
count = cursor.fetchall()
cursor.close()

return count