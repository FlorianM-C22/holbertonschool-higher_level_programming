#!/usr/bin/python3
"""
Unittest for rectangle.py


"""

import unittest
from models.rectangle import Rectangle as rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for rectangle.py
    """

    def test_id(self):
        """
        Test id
        """
        r1 = rectangle()
        self.assertEqual(r1.id, 1)
        r2 = rectangle()
        self.assertEqual(r2.id, 2)
        r3 = rectangle(12)
        self.assertEqual(r3.id, 12)
        r4 = rectangle()
        self.assertEqual(r4.id, 3)

    def test_to_json_string(self):
        """
        Test to_json_string
        """
        r1 = rectangle()
        self.assertEqual(r1.to_json_string(None), "[]")
        self.assertEqual(r1.to_json_string([]), "[]")
        self.assertEqual(r1.to_json_string([{'id': 89}]), '[{"id": 89}]')
        self.assertEqual(r1.to_json_string([{'id': 89}, {'id': 89}]),
                         '[{"id": 89}, {"id": 89}]')

    def test_from_json_string(self):
        """
        Test from_json_string
        """
        r1 = rectangle()
        self.assertEqual(r1.from_json_string(None), [])
        self.assertEqual(r1.from_json_string("[]"), [])
        self.assertEqual(r1.from_json_string('[{"id": 89}]'), [{'id': 89}])
        self.assertEqual(r1.from_json_string('[{"id": 89}, {"id": 89}]'),
                         [{'id': 89}, {'id': 89}])

    def test_save_to_file(self):
        """
        Test save_to_file
        """
        r1 = rectangle()
        r1.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    if __name__ == '__main__':
        unittest.main()
