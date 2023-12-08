import unittest
import os
from unittest.mock import patch
from lab_03 import *

class TestLab3(unittest.TestCase):
    def setUp(self):
        self.group_list = StudentList()
        self.test_data = [
        {'name': 'Mykola', 'phone': '06712345678', 'email': 'mykola@gmail.com', 'group': 'EM-191'},
        {'name': 'Zak', 'phone': '06712345678', 'email': 'zak@gmail.com', 'group': 'EM-191'},
        {'name': 'George', 'phone': '06712345678', 'email': 'george@gmail.com', 'group': 'EM-191'},
        {'name': 'Anna', 'phone': '06712345678', 'email': 'anna@gmail.com', 'group': 'EM-191'},
    ]


    def test_addNewElement(self):

        for data in self.test_data:
            with patch('builtins.input', side_effect=list(data.values())):
                self.group_list.addNewElement()

        self.assertEqual(self.group_list.list_students[2].name, 'Mykola')
        self.assertEqual(self.group_list.list_students[3].name, 'Zak')
        self.assertEqual(self.group_list.list_students[1].name, 'George')
        self.assertEqual(self.group_list.list_students[0].name, 'Anna')
                

    def test_updateElement(self):
        for data in self.test_data:
            with patch('builtins.input', side_effect=list(data.values())):
                self.group_list.addNewElement()

        self.assertEqual(self.group_list.list_students[2].name, 'Mykola')
        self.assertEqual(self.group_list.list_students[3].name, 'Zak')
        self.assertEqual(self.group_list.list_students[1].name, 'George')
        self.assertEqual(self.group_list.list_students[0].name, 'Anna')

        with patch('builtins.input', side_effect=['Anna', 'William', '06712345678', 'william@gmail.com', 'EM-192']):
            self.group_list.updateElement()
        self.assertEqual(self.group_list.list_students[2].name, "William")
        self.assertNotIn("Anna", [student.name for student in self.group_list.list_students])

    
    def test_deleteElement(self):
        for data in self.test_data:
            with patch('builtins.input', side_effect=list(data.values())):
                self.group_list.addNewElement()
        self.assertEqual(self.group_list.list_students[2].name, 'Mykola')
        self.assertEqual(self.group_list.list_students[3].name, 'Zak')
        self.assertEqual(self.group_list.list_students[1].name, 'George')
        self.assertEqual(self.group_list.list_students[0].name, 'Anna')
     
        with patch('builtins.input', side_effect=['Mykola']):
            self.group_list.deleteElement()
        self.assertNotIn("Mykola", [student.name for student in self.group_list.list_students])

    def test_save_csv(self):
        try:
            load_list_students = Utils.load_csv('test_lab3.csv')
            save_list_students = Utils.save_csv(load_list_students, 'test_lab3.csv')
            self.assertTrue(os.path.isfile('test_lab3.csv'))
            self.assertEqual(load_list_students, save_list_students)
        finally:
            pass

if __name__ == '__main__':
    unittest.main()
    