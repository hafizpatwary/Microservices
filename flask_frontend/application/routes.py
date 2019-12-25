from application import app
from flask import request, render_template
import requests
import json


@app.route('/', methods=["GET","POST"])
def quiz():

    package = requests.get('http://prize:5000').json()

    prize = package["prize"]
    image = package["image"]
    quiz_answers = package["options"]

    if request.method == 'POST':
        if request.form['answer'] == request.form['flag']:
            good = f"{request.form['flag']} {request.form['answer']} and {prize}"
        else:
            good = request.form['flag']

        return good


    return render_template("quiz.html", title="quiz", image=image.lower(), png=image, options=quiz_answers)

