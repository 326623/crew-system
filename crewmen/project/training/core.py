from flask import Flask, redirect, url_for, render_template, session, g, request, flash, Blueprint, abort, jsonify
from crewmen import app, login_required, power_required
import datetime
from models import *
from flask_nav import Nav
from flask_nav.elements import *
from .form import AddPlanForm, UpdateItemForm, AddPlanItemForm
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
    #should reorder or rewrite my js
    attr = [(row.attr_ID, row.attr_name) for row in TrainingItem.query.filter_by(item_name=item_name).first().attr]
    #print(attr)

    return jsonify(attr)

@training_blueprint.route('/add_plan', methods=['GET', 'POST'])
@login_required
@power_required
def add_plan():

    print("Hey There!!!\n")
    form = AddPlanForm()

    forms = [form.plan_ID, form.training_level, form.item_name, form.attr_name, form.comp]
    csrf_token = form.csrf_token


    # should add the validators in the future, no exception handling at all, running freely!!!
    if request.method == 'POST':
        print(form.train_at.data)
        print(form.training_last.data)

        plan_id = db.session.query(func.max(TrainingPlan.plan_ID)).scalar()
        if plan_id < form.plan_ID.data:
            new_plan = TrainingPlan(plan_ID=form.plan_ID.data,
                                    train_at=form.train_at.data,
                                    training_last=form.training_last.data,
                                    ID=session['login_ID'],
                                    training_level=form.training_level.data)

            db.session.add(new_plan)
            plan_id = form.plan_ID.data
        #ad.session.commit()

        newItem = TrainingItem.query.filter_by(item_name=form.item_name.data).first()
        item_id = newItem.item_ID
        newAttr = [ID.attr_ID for ID in newItem.attr]
        for i in range(len(newAttr)):
            new_req = RequirementInPlan(plan_ID=plan_id,
                                        item_ID=item_id,
                                        attr_ID=newAttr[i],
                                        comp=form.comp.data[i],
                                        requirement=form.attr_name.data[i]
            )

            db.session.add(new_req)


        db.session.commit()

        redirect(url_for('training.add_plan'))
    error = None

    return render_template('add_plan.html',
                           train_at=form.train_at,
                           training_last=form.training_last,
                           csrf_token=csrf_token, forms=forms)

@training_blueprint.route('/add_plan_item', methods=['GET', 'POST'])
@login_required
@power_required
def add_plan_item():
    form = AddPlanItemForm()

    if form.validate_on_submit():

        flash("You have added a new item to the plan")

    return render_template('add_plan_item.html', form=form)

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
