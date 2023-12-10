import unittest
from unittest.mock import patch
from lab_04 import *

class TestLab4(unittest.TestCase):
    def setUp(self):
        self.math_common_entries = [
    "3 + 4 * 2 / (1 - 5) ^ 2",        
    "2 ^ 3",
    "2 ^ 3 * 4",
    "2 * (3 + 4)"
    ]
        
        self.rpn_entries = [
    "3 4 2 * 1 5 - 2 ^ / +",
    "2 3 ^",
    "2 3 ^ 4 *",
    "2 3 4 + *"
        ]

        self.error_entries = [
    "abc12dj",
    "12rpn"
    ]
        self.results = [
            3.5,
            8,
            32,
            14
        ]

    def test_RPNGenerator(self):
        i = 0
        while i < len(self.math_common_entries):
            self.assertEqual(RPNGenerator(self.math_common_entries[i]), self.rpn_entries[i])
            i = i + 1

        self.assertEqual(RPNGenerator(self.error_entries[0]), "You entered something wrong! Please, try enter again.")
        self.assertEqual(RPNGenerator(self.error_entries[1]), "You entered something wrong! Please, try enter again.")


    def test_RPNCalculator(self):
        i = 0
        while i < len(self.rpn_entries):
            self.assertEqual(RPNCalculator(self.rpn_entries[i]), self.results[i])
            i = i + 1

        self.assertEqual(RPNCalculator(self.error_entries[0]), "You entered something wrong! Please, try enter again.")
        self.assertEqual(RPNCalculator(self.error_entries[1]), "You entered something wrong! Please, try enter again.")


if __name__ == '__main__':
    unittest.main()
    