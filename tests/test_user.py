import unittest
import sys
sys.path.append('src/models')
from user import User
from datetime import datetime

class TestUser(unittest.TestCase):
    def setUp(self):
     self.user = User()

    def test_all(self):
        self.assertIsInstance(self.user.all(),list)
        self.assertIsNotNone(self.user.all())

    def test_get(self):
        self.assertEqual(len(self.user.get(1)), 6)
        self.assertIsNotNone(self.user.get(1))
    
    def test_create(self):
        self.assertIsInstance(self.user.create('samson1','vero','ola'),tuple)
        self.assertEqual(len(self.user.create('samson1','vero','ola')), 6)
        self.assertIsNotNone(self.user.create('samson1','vero','ola'))
    
    def test_update(self):
        update_time = datetime.now()
        self.assertIsNotNone(self.user.update(33,'samson1','vero','ola'))
    
    def test_destroy(self):
        user_table_length = len(self.user.all())
        self.assertIsNotNone(self.user.destroy(1))
        self.assertTrue(user_table_length -1 != user_table_length)


    def tearDown(self):
        self.user = None