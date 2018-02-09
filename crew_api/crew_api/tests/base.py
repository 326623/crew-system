from flask_testing import TestCase
from crew_api import app, bcrypt, User, Member, db
from crew_api.config import TestConfig

import unittest
class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object(TestConfig)
        return app

    def setUp(self):
        print('\ncreating all tables')
        db.create_all()
        db.session.add(Member(name='admin', ID='1996', job='couch'))
        db.session.commit()

    def tearDown(self):
        print('dropping all tables')
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()
