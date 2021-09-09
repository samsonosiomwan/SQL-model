import unittest
import sys
from sqlite.crud_operations import CrudOperations



class CrudeOperations(unittest.TestCase):
    def setUp(self):
        self.crud = CrudOperations()

    def test_read_all(self):
        self.assertIsNotNone(self.crud.read_all())
        self.assertIsInstance(self.crud.read_all(),list)
    
    def test_create(self):
        self.assertIsNotNone(self.crud.create(last_name = 'samson',first_name ='osiomwan',SSN = '123-45-6789', Test1 =50.1, Test2 = 50.1, Test3 = 50.2, Test4 = 50.3, Final = 50.1, Grade = 'D-'))
        self.assertIsInstance(self.crud.create(),list)
    
    def test_get_passed(self):
        self.assertIsNotNone(self.crud.get_passed())
        self.assertIsInstance(self.crud.get_passed(),str)
    
    def test_get_passed(self):
        self.assertIsNotNone(self.crud.get_failed())
        self.assertIsInstance(self.crud.get_failed(),str)
    
    def test_get_test1(self):
        self.assertIsNotNone(self.crud.get_test1())
        self.assertIsInstance(self.crud.get_test1(),str)
    
    def test_update(self):
        self.assertIsNotNone(self.crud.update(40,50,57,69,79,'D','123-45-6789'))
        self.assertIsInstance(self.crud.update(40,50,57,69,79,'D','123-45-6789'),list)
    
    def test_destroy(self):
        self.assertIsNotNone(self.crud.destroy('123-45-6789'))
        self.assertIsInstance(self.crud.destroy('123-45-6789'),list)

    def tearDown(self):
        self.crud = None