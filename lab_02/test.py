import unittest
import os
from unittest.mock import patch
from lab_02 import *

class TestLab2(unittest.TestCase):
    def setUp(self):
        self.list_students = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@gmail.com", "group": "CS-221"},
    {"name": "Emma", "phone": "0637457545", "email": "emma@gmail.com", "group": "CS-221"},
    {"name": "Michael", "phone": "0994747444", "email": "michael@gmail.com", "group": "AB-219"},
    {"name": "Zak", "phone": "0635545467", "email": "zak@gmail.com", "group": "CE-221"},
]
        
    def test_addNewElement(self):
        with patch('builtins.input', side_effect=['Denys', '0673838838', 'denys@gmail.com', 'CS-221']):
            addNewElement(self.list_students)
        self.assertEqual(self.list_students[1]["name"], "Denys")
    

    def test_updateElement(self):
        with patch('builtins.input', side_effect=['Emma', 'William', '06757577575', 'william@gmail.com', 'CS-221']):
            updateElement(self.list_students)
        self.assertEqual(self.list_students[2]["name"], "William")
        self.assertNotIn({"name": "Emma", "phone": "0637457545", "email": "emma@gmail.com", "group": "CS-221"}, self.list_students)
        
    
    def test_deleteElement(self): 
        with patch('builtins.input', side_effect=['Michael']):
            deleteElement(self.list_students)
        self.assertNotIn({"name": "Michael", "phone": "0994747444", "email": "michael@gmail.com", "group": "AB-219"}, self.list_students)


    def test_save_csv(self):
        try:
            save_csv('test_lab2.csv', self.list_students)
            self.assertTrue(os.path.isfile('test_lab2.csv'))
            data = load_csv('test_lab2.csv')
            self.assertEqual(data, self.list_students)
        finally:
            pass


if __name__ == '__main__':
    unittest.main()
    