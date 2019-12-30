from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from application.models import Prize


class PrizeForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=1, max=64)])
    prize = HiddenField(validators=[DataRequired()])
    submit = SubmitField('Retrieve')

    def validate_email(self, email):
        email = Prize.query.filter_by(email=email.data).first()

        if email:
            raise ValidationError('Email already used to retrieve a prize!')
