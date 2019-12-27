from application import app, db
from flask import request, render_template, url_for, redirect
from application.models import Prize, Countries, Answers
import requests


@app.route('/', methods=["GET"])
def quiz():
    response = requests.get('http://localhost:5001')

    if response.status_code == 200:
        quiz = response.json()
        image = quiz["image"]
        quiz_options = quiz["options"]

        return render_template("quiz.html", title="quiz", image=image.lower(), png=image, options=quiz_options)
    return "Not OK"



@app.route('/outcome', methods=["POST"])
def outcome():
    response = requests.get('http://localhost:80')

    if response.status_code == 200:
        prize = response.json()["prize"]
        answer = request.form['answer']
        flag = request.form['flag']
        correct = True if answer == flag else False

        if correct:
            outcome = f"Correct! You are eligible for £ {prize}0 off on your next booking with YeezyJet"
            link = "retrieve"
        else:
            outcome = "Unlucky, try again by clicking the link below!"
            link = "quiz"

        answerData = Answers(
            correct=correct,
            flag=Countries.query.get_or_404(flag)
            )
        db.session.add(answerData)
        db.session.commit()

        return render_template("outcome.html", outcome=outcome, link=link)
    return redirect(url_for('quiz'))

# Store prize
# Ask for email and store with prize

