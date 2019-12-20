from flask import Flask 
import requests
import json

app = Flask(__name__)

@app.route('/quiz', methods="GET")
def quiz():
	