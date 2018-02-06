from crew_api.models import metadata, AttrInItem, FeeLog, ItemAttribute, Member
from crew_api.tests.Base import BaseTestCase
import unittest

class FlaskTestCase(BaseTestCase):
    # ensure api was set up properly
    def test_doc(self):
        response = self.client.get('/')
        self.assertIn(b'API', response.data)

if __name__ == '__main__':
    unittest.main()
