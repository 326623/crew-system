from flask_testing import TestCase
from crew_api.main import app, db
#from crew_api.memory_table import Base
from crew_api.config import TestConfig

import unittest
#import flask_testing


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object(TestConfig)
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()
