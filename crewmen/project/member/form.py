from flask_wtf import FlaskForm, RecaptchaField
from wtforms import BooleanField, StringField, PasswordField, validators, RadioField, SelectField, DecimalField, DateTimeField, FieldList, SubmitField
from wtforms_components import DateRange, TimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired
from datetime import datetime
from decimal import Decimal
from models import *

class AddMemberForm(FlaskForm):
    name = StringField(
        'Member name',
        validators=[InputRequired()]
    )

    sex = SelectField(
        'Sex',
        choices=[('男', '男'), ('女', '女')],
        validators=[InputRequired()]
    )

    enter_club = DateTimeField(
        'Date(%Y-%m-%d %H:%M:%S)',
        format='%Y-%m-%d %H:%M:%S',
        default=datetime.today
    )

    ID = DecimalField(
        'ID number',
        validators=[InputRequired(message='Not a valid ID, Please enter again')]
    )

    submit = SubmitField(
        'submit'
    )

class DeleteMemberForm(FlaskForm):
    ID =  DecimalField(
        'ID number',
        validators=[InputRequired(message='Not a valid ID, Please enter again')]
    )

    submit = SubmitField(
        'submit'
    )
