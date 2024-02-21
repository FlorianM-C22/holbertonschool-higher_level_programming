#!/usr/bin/python3
"""
Unittest for Base class


"""


import unittest
import os
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for Base class
    """

    def test_id(self):
        """
        Test id assignment
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_id_is_none(self):
        """
        Test id when it is None
        """
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)

    def test_id_is_string(self):
        """
        Test id when it is a string
        """
        b = Base("1")
        self.assertEqual(b.id, "1")

    def test_id_is_zero(self):
        """
        Test id when it is zero
        """
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_is_negative(self):
        """
        Test id when it is negative
        """
        b = Base(-1)
        self.assertEqual(b.id, -1)

    def test_id_is_boolean(self):
        """
        Test id when it is a boolean
        """
        b = Base(True)
        self.assertEqual(b.id, True)

    def test_id_is_float(self):
        """
        Test id when it is a float
        """
        b = Base(1.1)
        self.assertEqual(b.id, 1.1)

    def test_id_is_complex(self):
        """
        Test id when it is a complex number
        """
        b = Base(1+2j)
        self.assertEqual(b.id, 1+2j)

    def test_id_is_list(self):
        """
        Test id when it is a list
        """
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def test_id_is_dict(self):
        """
        Test id when it is a dictionary
        """
        b = Base({'id': 1})
        self.assertEqual(b.id, {'id': 1})

    def test_to_json_string(self):
        """
        Test to_json_string method
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        """
        Test from_json_string method
        """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 12}]'), [{'id': 12}])

    def test_to_json_string_empty_list(self):
        """
        Test to_json_string method with an empty list
        """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_single_dictionary(self):
        """
        Test to_json_string method with a single dictionary
        """
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_save_to_file_none(self):
        """
        Test save_to_file method with None as input
        """
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """
        Test save_to_file when list_objs is None
        """
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Base.json")

    def test_save_to_file_with_non_base_objects(self):
        """
        Test save_to_file with non-Base objects in list_objs
        """
        with self.assertRaises(AttributeError):
            Base.save_to_file([1, "string", 3.14, True])

    def test_save_to_file_empty_list(self):
        """
        Test save_to_file method with an empty list as input
        """
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_from_json_string_none(self):
        """
        Test from_json_string method with None as input
        """
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_string(self):
        """
        Test from_json_string method with an empty string as input
        """
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_single_dictionary(self):
        """
        Test from_json_string method with a single dictionary as input
        """
        self.assertEqual(Base.from_json_string('[{"id": 12}]'), [{'id': 12}])

    def test_load_from_file_none(self):
        """
        Test load_from_file method with None as input
        """
        self.assertEqual(Base.load_from_file(), [])


if __name__ == '__main__':
    unittest.main()
