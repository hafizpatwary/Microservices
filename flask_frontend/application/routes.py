from application import app, db
from flask import request, render_template, url_for, redirect
from application.models import Prize, Countries, Answers
from application.forms import PrizeForm
import requests


@app.route('/', methods=["GET"])
def quiz():
    response = requests.get('http://localhost:5001')

    if response.status_code == 200:
        quiz = response.json()
        image = quiz['image']
        quiz_options = quiz['options']

        return render_template("quiz.html", title="quiz", image=image.lower(), png=image, options=quiz_options)
    return "Not OK"



@app.route('/outcome', methods=["GET","POST"])
def outcome():
    response = requests.get('http://localhost:80')

    if response.status_code == 200 and request.method == "POST":
        prize = response.json()['prize']
        answer = request.form['answer']
        flag = request.form['flag']
        correct = True if answer == flag else False

        if correct:
            outcome = f"Correct! You are eligible for £ {prize}0 off on your next booking with YeezyJet"
        else:
            outcome = "Unlucky, try again by clicking the link below!"

        answerData = Answers(
            correct=correct,
            flag=Countries.query.get_or_404(flag)
            )
        db.session.add(answerData)
        db.session.commit()

        return render_template("outcome.html", outcome=outcome, correct=correct, prize=prize)
    return redirect(url_for('quiz'))



@app.route('/retrieve', methods=["POST"])
def retrieve():
    prize = request.form['prize']
    form = PrizeForm(prize=prize)

    if form.validate_on_submit():
        prizeData = Prize(
            email=form.email.data,
            prize=form.prize.data
            )
        db.session.add(prizeData)
        db.session.commit()
        return redirect(url_for('quiz'))
    else:
        print(form.errors)

    return render_template("retrieve.html", form=form)






# Store prize
# Ask for email and store with prize
# Create form


