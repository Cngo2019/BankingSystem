from flask import Flask
from flask_mysqldb import MySQL
from dotenv import load_dotenv

import os
app = Flask(__name__)


app.config['MYSQL_HOST'] = os.getenv('HOST')
app.config['MYSQL_USER'] = os.getenv('USER')
app.config['MYSQL_PASSWORD'] = os.getenv('PASSWORD')
app.config['MYSQL_DB'] = os.get('DB')
mysql = MySQL(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"