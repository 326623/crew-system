from crew_api.models import metadata, User, AttrInItem, FeeLog, ItemAttribute, Member
from crew_api.tests.Base import BaseTestCase
from flask import json
import unittest

class FlaskTestCase(BaseTestCase):
    # ensure api was set up properly
    def test_doc(self):
        response = self.client.get('/')
        self.assertIn(b'API', response.data)

        response = self.client.get('/api/v1', follow_redirects=True)
        self.assertIn(b'Rowing Crew API', response.data)

    def test_user(self):
        response = self.client.get('/api/v1/user/0')
        print(response.data)
        self.assertEqual(b'{\n    "email": null,\n    "ID": null,\n    "username": null\n}\n',
                         response.data)

if __name__ == '__main__':
    unittest.main()
