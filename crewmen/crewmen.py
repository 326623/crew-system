import os
import sqlite3
import pymysql
from flask import Flask, redirect, url_for, render_template, session, g, request, flash, Blueprint, abort
from jinja2 import TemplateNotFound
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from init_crew import init_db
from flask_nav import Nav
from flask_nav.elements import *

########################
### helper function ####
########################

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('user.login'))
    return wrap

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


##########################
### Initialize the app ###
##########################


def Init_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    Bootstrap(app)
    return app

app = Init_app()
db = SQLAlchemy(app)
from models import *
from project.user.core import user_blueprint
from project.training.core import training_blueprint
from project.member.core import member_blueprint
from project.fee.core import fee_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(training_blueprint)
app.register_blueprint(member_blueprint)
app.register_blueprint(fee_blueprint)

############################
### The navigation panel ###
############################


nav = Nav()
@nav.navigation()
def top():

    # no nav for register.html

    items = [View('home', 'home')]
    user_sub_list = [View('Log out', 'user.logout'),
                     View('Change Password', 'user.password_update'),]

    training_sub_list = [View('Training', 'training.show_training_plan'),
                         View('Training Item', 'training.show_item'),]

    fee_sub_list = [View('Show Fee Log', 'fee.show_fee_log'),
                    View('Add Fee Log', 'fee.add_fee_log'),]

    member_sub_list = [View('Profile', 'member.member_profile'),]


    if session['login_job'] in ['crew leader', 'couch']:
        training_sub_list += [View('Add Training plan', 'training.add_plan'),
                              View('Add Training item', 'training.add_item'),]

        member_sub_list += [View('Add New Member ', 'member.add_member'),
                            View('Delete Member', 'member.delete_member'),
                            View('Show all member profile', 'member.allmember_profile'),]
    else:
        # do nothing ...
        1

    items = items + [Subgroup('User', *user_sub_list),
                     Subgroup('Training', *training_sub_list),
                     Subgroup('Member', *member_sub_list),
                     Subgroup('Fee', *fee_sub_list)]

    return Navbar('Home', *items)
nav.init_app(app)


@app.route('/home')
@login_required
def home():
    return render_template('home.html', error=None)

@app.route('/')
def welcome():
    return render_template('welcome.html', error=None)

@app.cli.command('initdb')
def initdb_command():
    """ This would drop all table and reconstruct the schema is mysql"""
    init_db()
    print("All table drop and initialized")
