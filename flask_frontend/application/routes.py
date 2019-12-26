from application import app
from flask import request, render_template, url_for, redirect
import requests
import json


@app.route('/', methods=["GET"])
def quiz():

    response = requests.get('http://localhost:5001').json()
    #prize = response["prize"]
    image = response["image"]
    quiz_options = response["options"]

    return render_template("quiz.html", title="quiz", image=image.lower(), png=image, options=quiz_options)

@app.route('/outcome', methods=["POST"])
def outcome():
    response = requests.get('http://localhost:80').json()
    prize = response["prize"]
    if request.form['answer'] == request.form['flag']:
        outcome = f"Correct! You are eligible for £ {prize}0 off on your next booking with YeezyJet"
        link = "retrieve"
    else:
        outcome = f"Unlucky, try again by refreshing the page!"
        link = "quiz"

    return render_template("outcome.html", outcome=outcome, link=link)


