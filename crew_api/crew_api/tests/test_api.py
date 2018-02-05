from flask_testing import TestCase
from crew_api import app, db, TestConfig
from crew_api.models import metadata, AttrInItem, FeeLog, ItemAttribute, Member
#app=crew_api.app
#db=crew_api.db
#TestConfig=crew_api.TestConfig


import unittest
#import flask_testing


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object(TestConfig)
        return app

    def setUp(self):
        print(db)
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_something(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
