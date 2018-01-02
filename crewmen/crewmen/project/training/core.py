from flask import Flask, redirect, url_for, render_template, session, g, request, flash, Blueprint, abort, jsonify
from crewmen import app, login_required, wraps
import datetime
from models import *
from flask_nav import Nav
from flask_nav.elements import *
from .form import *
##################
### Navbar init###
##################

training_blueprint = Blueprint(
    'training', __name__,
    template_folder='templates'
)

########################
### helper function ####
########################

def power_required(f):
    @wraps(f)
    def wrap(*arg, **kwargs):
        job = session['login_job']
        if job == 'crew leader' or job == 'couch':
            return f(*arg, **kwargs)
        else:
            flash('You have no power.')
            return redirect(url_for('home'))
    return wrap

########################
########################
########################



@training_blueprint.route('/show_item')
@login_required
def show_item():
    items = TrainingItem.query.all()
    return render_template('show_item.html', items=items)

@training_blueprint.route('/_get_attr/')
@login_required
@power_required
def _get_attr():
    item_name = request.args.get('item_name', '01', type=str)

    print("from get attr:", item_name)
    #print(item_name)
    attr = [(row.attr_ID, row.attr_name) for row in TrainingItem.query.filter_by(item_name=item_name).first().attr]
    #print(attr)

    return jsonify(attr)

@training_blueprint.route('/add_plan', methods=['GET', 'POST'])
@login_required
@power_required
def add_plan():

    print("Hey There!!!\n")
    form = AddPlanForm()

    forms = [form.training_level, form.item_name, form.attr_name, form.comp]
    csrf_token = form.csrf_token

    print(form.validate())

    print(form.training_level.data)
    print(form.item_name.data)
    print(form.attr_name.data)
    print(form.comp.data)
    if form.validate_on_submit():
        new_plan = TrainingPlan()
        plan_req = RequirementInPlan();
        plan_req.plan_ID = 1# need to query database for this
        #plan_req.item_ID = TrainingItem.query.filter_by(item_name=form.item_name.data).first().item_ID

        # a for loop
        # for x in form.temp_name.data:
        #     print(x)
            #plan_req.attr_ID = 

        print(request.form)
        #print(form.temp_name.data)

        redirect(url_for('training.add_plan'))
    error = None

    return render_template('add_plan.html', csrf_token=csrf_token, forms=forms)

@training_blueprint.route('/add_item', methods=['GET', 'POST'])
@login_required
@power_required
def add_item():
    form = UpdateItemForm()
    forms = [form.item_name, form.is_strength, form.is_test]

    if form.validate_on_submit():
        item = TrainingItem(item_name=form.item_name.data,
                            is_strength=form.is_strength.data,
                            is_test=form.is_test.data)

        db.session.add(item)
        db.session.commit()
        flash("You have added an item.")
        return render_template('add_item.html', forms=forms, form=form)

    return render_template('add_item.html', forms=forms, form=form)


@training_blueprint.route('/training_plan')
@login_required
def show_training_plan():
    today = datetime.date.today()
    nextday = today + datetime.timedelta(days=1)
    today_plan = TrainingPlan.query.filter(TrainingPlan.train_at >= today, TrainingPlan.train_at < nextday).all()
    return render_template('training_plan.html', plans=today_plan)



# <!-- {% for plan in strength_plan %}
#      <strong>plan_ID:</strong>{{ plan.plan_ID }}<br>
#      <strong>training_level:</strong>{{ plan.training_level }}<br>
#      <strong>training_time:</stro


# ng>{{ plan.training_last }}<br>
#      {% for item in plan.requirement %}
#      <strong>item_ID</strong>{{ plan.items.item_ID }}<br>
#      <strong>item time</strong>{{ plan.items.item_name }}<br>
#      {% if item.is_strength == 'y' %}
#      <strong>This is the strength section</strong>
#      {% else %}
#      <strong>This is the aerobic section</strong>
#      {% endif %}
#      {% endfor%}
#      {% endfor %} -->
