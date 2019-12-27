from application import db
from datetime import datetime

class Prize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prize =  db.Column(db.Float)
    email = db.Column(db.String(64), nullable=False, unique=True)
    # country = db.Column(db.String(512), nullable=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"id: {self.id} \r\nPrize: {self.prize} \r\nemail: {self.email} \r\ndate: {self.date}"

class Countries(db.Model):
    country_id = db.Column(db.String(6), primary_key=True)
    country = db.Column(db.String(44))
    quiz_answers = db.relationship('Answers', backref='flag')

    def __repr__(self):
        return f"Country_Code: {self.country_id} \r\nCountry: {self.country}"

class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    correct = db.Column(db.Boolean, nullable=False)
    country = db.Column(db.String(6), db.ForeignKey('countries.country_id'))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Correct: {self.correct} \r\nCountry: {self.country} \r\ndate: {self.date}"









