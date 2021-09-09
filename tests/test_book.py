import unittest
import sys
sys.path.append('src/models')
from book import Book
from datetime import datetime


class TestBook(unittest.TestCase):
    def setUp(self):
        self.users_book = Book()
    
    def test_all(self):
        self.assertIsInstance(self.users_book.all(1),list)
        self.assertIsNotNone(self.users_book.all(1))
    
    def test_get(self):
        self.assertIsInstance(self.users_book.get(1),tuple)
        self.assertEqual(len(self.users_book.get(1)), 6)
        self.assertIsNotNone(self.users_book.get(1))
    
    def test_create(self):
        self.assertIsInstance(self.users_book.create(1,'veronica',50),tuple)
        self.assertEqual(len(self.users_book.create(1,'romeo and julie',50)), 6)
        self.assertIsNotNone(self.users_book.create(1,'vero',20))
    
    def test_update(self):
        update_time = datetime.now()
        self.assertIsNotNone(self.users_book.update(39,1,'tomama',10))

    def test_destroy(self):
        self.assertIsNotNone(self.users_book.destroy(1))

    def tearDown(self):
        self.users_book = None
    