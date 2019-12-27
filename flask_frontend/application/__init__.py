from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{getenv('MYSQL_USERNAME')}:{getenv('MYSQL_PASSWORD')}@{getenv('MYSQL_IP')}/quiz"

db = SQLAlchemy(app)

from application import routes
