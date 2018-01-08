from flask_wtf import FlaskForm, RecaptchaField
from wtforms import BooleanField, StringField, PasswordField, validators, RadioField, SelectField, DecimalField, DateTimeField, FieldList, SubmitField
from wtforms_components import DateRange, TimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired
from decimal import Decimal
from models import *
from datetime import datetime

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

    plan_ID = DecimalField(default=Decimal(db.session.query(func.max(TrainingPlan.plan_ID)).scalar()) + 1,
                           label='plan_ID')

    train_at = DateTimeField(
        'Date(%Y-%m-%d %H:%M:%S)',
        format='%Y-%m-%d %H:%M:%S',
        validators=[DateRange(min=None, max=None)],
        default = datetime.today
    )

    training_last = TimeField(
        'Lasting(%H:%M)',
        format='%H:%M',
        validators=[DateRange(min=None, max=None)]
    )

    training_level = SelectField(
        'training level',
        choices=[(c,c) for c in ['newbie', 'medium', 'old bird', 'all']],
        validators=[InputRequired()]
    )

    attr_name = FieldList(
        DecimalField(default=Decimal('-1')),
        label='Attribute Value',
        min_entries=ItemAttribute.query.count()
    )

    comp = FieldList(
        SelectField(default=('Not picked', 'Not picked'), choices=[('larger', 'larger'), ('smaller', 'smaller')]),
        min_entries=ItemAttribute.query.count()
    )

    # comp = SelectField(
    #     'comp',
    #     choices=[('larger', 'larger'), ('smaller', 'smaller')],
    #     validators=[InputRequired()]
    # )

    item_name = SelectField(
        'Item Name',
        choices=[(c.item_name, c.item_name) for c in TrainingItem.query.all()]
    )



    #for attr in TrainingItem.query().attr:

class AddPlanItemForm(FlaskForm):
    plan_ID = DecimalField(default=Decimal(db.session.query(func.max(TrainingPlan.plan_ID)).scalar()),
                           label='plan_ID')

    training_level = SelectField(
        'training level',
        choices=[(c,c) for c in ['newbie', 'medium', 'old bird', 'all']],
        validators=[InputRequired()]
    )

    attr_name = FieldList(
        DecimalField(default=Decimal('-1')),
        label='Attribute Value',
        min_entries=ItemAttribute.query.count()
    )

    comp = FieldList(
        SelectField(default='Not required', choices=[('larger', 'larger'), ('smaller', 'smaller'), ('Not required', 'Not required')]),
        min_entries=ItemAttribute.query.count()
    )

    # comp = SelectField(
    #     'comp',
    #     choices=[('larger', 'larger'), ('smaller', 'smaller')],
    #     validators=[InputRequired()]
    # )

    item_name = SelectField(
        'Item Name',
        choices=[(c.item_name, c.item_name) for c in TrainingItem.query.all()]
    )

    submit = SubmitField( )
