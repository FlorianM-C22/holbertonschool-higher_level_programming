#!/usr/bin/python3
"""
Unittest for base.py


"""

import unittest

base = __import__('models.base').Base


class TestBase(unittest.TestCase):
    """
    Test cases for base.py
    """

    def test_id(self):
        """
        Test id
        """
        b1 = base()
        self.assertEqual(b1.id, 1)
        b2 = base()
        self.assertEqual(b2.id, 2)
        b3 = base(12)
        self.assertEqual(b3.id, 12)
        b4 = base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """
        Test to_json_string
        """
        b1 = base()
        self.assertEqual(b1.to_json_string(None), "[]")
        self.assertEqual(b1.to_json_string([]), "[]")
        self.assertEqual(b1.to_json_string([{'id': 89}]), '[{"id": 89}]')
        self.assertEqual(b1.to_json_string([{'id': 89}, {'id': 89}]),
                         '[{"id": 89}, {"id": 89}]')

    def test_from_json_string(self):
        """
        Test from_json_string
        """
        b1 = base()
        self.assertEqual(b1.from_json_string(None), [])
        self.assertEqual(b1.from_json_string("[]"), [])
        self.assertEqual(b1.from_json_string('[{"id": 89}]'), [{'id': 89}])
        self.assertEqual(b1.from_json_string('[{"id": 89}, {"id": 89}]'),
                         [{'id': 89}, {'id': 89}])

    def test_save_to_file(self):
        """
        Test save_to_file
        """
        b1 = base()
        b1.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        b1.save_to_file([])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        b1.save_to_file([{'id': 89}])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 89}]')
        b1.save_to_file([{'id': 89}, {'id': 89}])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 89}, {"id": 89}]')

    def test_create(self):
        """
        Test create
        """
        b1 = base()
        b2 = b1.create()
        self.assertEqual(b2.id)
