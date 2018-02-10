import click
import unittest
from crew_api import app, db, bcrypt
from crew_api.models import *

def call_insert_data():
    conn=db.engine.connect()
    """ to be called to insert data without shackles of decorators """
    from crew_api.database_data import insert_member, \
        insert_users, insert_training_items, insert_attr_in_item, \
        insert_training_plan, insert_requirement_in_plan, insert_item_attr
    db.session.add_all(insert_member)
    db.session.commit()

    db.session.add_all(insert_users)
    db.session.commit()

    db.session.add_all(insert_training_items)
    db.session.commit()

    #db.session.add_all()
    conn.execute(ItemAttribute.__table__.insert(), insert_item_attr)
    conn.execute(AttrInItem.__table__.insert(), insert_attr_in_item)
    conn.execute(TrainingPlan.__table__.insert(), insert_training_plan)
    conn.execute(RequirementInPlan.__table__.insert(), insert_requirement_in_plan)
    #db.session.commit()
    #db.session.add_all([])
    click.echo('data inserted')

def call_init_db():
    click.echo('create all tables')
    db.create_all()
    click.echo('all tables created')

def call_drop_db():
    click.echo('drop all tables')
    db.drop_all()
    click.echo('all tables dropped')

@app.cli.command()
def test():
    """ Runs the testing """
    tests = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.cli.command()
def init_db():
    """ Initialize the Database, after drop_db """
    call_init_db()

@app.cli.command()
def drop_db():
    """ Clean up database """
    call_drop_db()

@app.cli.command()
def insert_data():
    """ Insert template data """
    call_insert_data()

@app.cli.command()
def rebuild():
    """ rebuild database with premade values"""
    call_drop_db()
    call_init_db()
    call_insert_data()


