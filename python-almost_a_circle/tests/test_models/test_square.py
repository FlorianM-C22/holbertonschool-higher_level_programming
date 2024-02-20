#!/usr/bin/python3
"""
Unittest for square.py


"""

import unittest
from models.square import Square as square


class TestSquare(unittest.TestCase):
    """
    Test cases for square.py
    """

    def test_id(self):
        """
        Test id
        """
        s1 = square()
        self.assertEqual(s1.id, 1)
        s2 = square()
        self.assertEqual(s2.id, 2)
        s3 = square(12)
        self.assertEqual(s3.id, 12)
        s4 = square()
        self.assertEqual(s4.id, 3)

    def test_to_json_string(self):
        """
        Test to_json_string
        """
        s1 = square()
        self.assertEqual(s1.to_json_string(None), "[]")
        self.assertEqual(s1.to_json_string([]), "[]")
        self.assertEqual(s1.to_json_string([{'id': 89}]), '[{"id": 89}]')
        self.assertEqual(s1.to_json_string([{'id': 89}, {'id': 89}]),
                         '[{"id": 89}, {"id": 89}]')

    def test_from_json_string(self):
        """
        Test from_json_string
        """
        s1 = square()
        self.assertEqual(s1.from_json_string(None), [])
        self.assertEqual(s1.from_json_string("[]"), [])
        self.assertEqual(s1.from_json_string('[{"id": 89}]'), [{'id': 89}])
        self.assertEqual(s1.from_json_string('[{"id": 89}, {"id": 89}]'),
                         [{'id': 89}, {'id': 89}])

    def test_save_to_file(self):
        """
        Test save_to_file
        """
        s1 = square()
        s1.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_create(self):
        """
        Test create
        """
        s1 = square()
        s1_dict = s1.to_dictionary()
        s2 = square.create(**s1_dict)
        self.assertEqual(s1 is s2, False)
        self.assertEqual(s1 == s2, False)
        self.assertEqual(s1.to_dictionary() == s2.to_dictionary(), True)

    def test_load_from_file(self):
        """
        Test load_from_file
        """
        s1 = square()
        s1.save_to_file(None)
        s2 = square.load_from_file()
        self.assertEqual(s1 is s2, False)
        self.assertEqual(s1 == s2, False)

    if __name__ == '__main__':
        unittest.main()
