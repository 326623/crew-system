import click
import unittest
from crew_api.main import app, db

@app.cli.command()
def test():
    """ Runs the testing """
    tests = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.cli.command()
def init_db():
    """ Initialize the Database, after drop_db """
    click.echo('Not implemented')

@app.cli.command()
def drop_db():
    """ Clean up database """
    click.echo('Not implemented')

@app.cli.command()
def insert_data():
    """ Insert template data """
    # db.session.add_all([
    #     User
    # ])

    click.echo('Not implemented')
