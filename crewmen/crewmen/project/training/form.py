from flask_wtf import FlaskForm, RecaptchaField
from wtforms import BooleanField, StringField, PasswordField, validators, RadioField, SelectField, DecimalField, DateTimeField, FieldList
from wtforms_components import DateRange
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired
from models import *

class UpdateItemForm(FlaskForm):
    item_name = StringField(
        'The name of the item',
        validators=[InputRequired()]
    )
    is_strength = RadioField(
        'Is it strength',
        choices=[('y', 'Yes'), ('n', 'No')],
        validators=[InputRequired()]
    )
    is_test = RadioField(
        'Is it test',
        choices=[('y', 'Yes'), ('n', 'No')],
        validators=[InputRequired()]
    )

class AddPlanForm(FlaskForm):
    # train_at = DateTimeField(
    #     'Date',
    #     format='%Y-%m-%d %H:%M:%S',
    #     validators=[DateRange(min=None, max=None)]
    # )

    # training_last = DateTimeField(
    #     'Lasting',
    #     format='%H:%M',
    #     validators=[DateRange(min=None, max=None)]
    # )

    training_level = SelectField(
        'training level',
        choices=[(c,c) for c in ['newbie', 'medium', 'old bird', 'all']],
        validators=[InputRequired()]
    )

    temp_name = FieldList(
        DecimalField(), label='testing', min_entries=1
    )

    attr_name = SelectField(
        'Attr Name',
        choices=[(row.attr_name, row.attr_name) for row in ItemAttribute.query.all()],
        validators=[InputRequired()]
    )

    comp = SelectField(
        'comp',
        choices=[('larger', 'larger'), ('smaller', 'smaller')],
        validators=[InputRequired()]
    )

    item_name = SelectField(
        'Item Name',
        choices=[(c.item_name, c.item_name) for c in TrainingItem.query.all()]
    )



    #for attr in TrainingItem.query().attr:

