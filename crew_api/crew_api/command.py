import click
import unittest
from crew_api import app, db, bcrypt
from crew_api.models import *


@app.cli.command()
def test():
    """ Runs the testing """
    tests = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.cli.command()
def init_db():
    """ Initialize the Database, after drop_db """
    db.create_all()

@app.cli.command()
def drop_db():
    """ Clean up database """
    db.drop_all()

@app.cli.command()
def insert_data():
    """ Insert template data """
    # db.session.add_all([
    #     User
    # ])

    click.echo(db)
    db.session.add_all(
        [Member(name='于H', ID='0', training_level='old bird'),
        Member(name='郭D胜', ID='1', training_level='old bird'),
        Member(name='X德昊', ID='2', training_level='old bird'),
        Member(name='S炜焜', ID='3', training_level='old bird'),
        Member(name='happygirlzt', ID='520', training_level='old bird'),
        Member(name='normal', ID='1997', training_level='newbie')]
    )
    db.session.commit()

    #db.session.add_all([])
    click.echo('data inserted')
#    click.echo('Not implemented')
