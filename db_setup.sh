#!/bin/bash
# Setting a virtualenvironment and installing dependencies
. ~/.bashrc
cd $(pwd)/flask_frontend
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Set up tables in database

python3 << EOF
import os
from pymysql import connect


connection = connect(
    host = os.getenv('MYSQL_IP'),
    user = os.getenv('MYSQL_USERNAME'),
    password = os.getenv('MYSQL_PASSWORD')
)

with connection.cursor() as cursor:
	cursor.execute('CREATE DATABASE IF NOT EXISTS yeezyjet')

# Creating tables and adding data to it
from application import db
from application.models import Answers, Countries, Prize


db.drop_all()
db.create_all()

connection = connect(
    host = os.getenv('MYSQL_IP'),
    user = os.getenv('MYSQL_USERNAME'),
    password = os.getenv('MYSQL_PASSWORD'), database = 'yeezyjet'
)

try:
    f = open('country_sql.txt', 'r')
    file = f.read()

    with connection.cursor() as cursor:
        cursor.execute(file)
        connection.commit()

finally:
    f.close()
    connection.close()

exit()
EOF

# Retun to root of project
deactivate
rm -rf venv
cd ../
