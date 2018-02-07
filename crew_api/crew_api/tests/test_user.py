from crew_api.models import metadata, User, AttrInItem, FeeLog, ItemAttribute, Member
from crew_api.tests.base import BaseTestCase, db, User, bcrypt
from flask import json
import unittest
print(db)

class FlaskTestCase(BaseTestCase):
    """ Calling self.client => flask.testing.FlaskClient """

    # ensure api was set up properly
    def test_doc(self):
        response = self.client.get('/')
        self.assertIn(b'API', response.data)

        response = self.client.get('/api/v1', follow_redirects=True)
        self.assertIn(b'Rowing Crew API', response.data)

    def test_user(self):
        response = self.client.get('/api/v1/user/0')
        self.assertEqual(dict(ID = None, email = None, username = None),
                         response.json)

        db.session.add(User(username='admin', password=bcrypt.generate_password_hash('admin'), ID='1996', email = 'hello@happygirlzt.com'))
        db.session.commit()
        pw_hash=db.session.query(User).filter(User.username=='admin').first().password
        print(bcrypt.check_password_hash(pw_hash, 'admin'))

if __name__ == '__main__':
    unittest.main()
