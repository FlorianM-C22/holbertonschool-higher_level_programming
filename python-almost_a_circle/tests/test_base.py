#!/usr/bin/python3
"""
Unittest for Base class


"""


import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle as Rectangle
from models.square import Square as Square


class TestBase(unittest.TestCase):
    """
    Test cases for Base class
    """

    def test_id(self):
        """
        Test id assignment
        """
        b1 = Base()
        self.assertEqual(b1.id, 3)
        b2 = Base()
        self.assertEqual(b2.id, 4)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 5)

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

    def test_id_tuple(self):
        """
        Test id when it is a tuple
        """
        b = Base((8,))
        self.assertEqual((8,), b.id)

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

    def test_to_json_string_empty_string(self):
        """
        Test to_json_string method with an empty string
        """
        self.assertEqual(Base.to_json_string(""), '""')

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

    def test_create_rectangle(self):
        """
        Test create method with a dictionary of attributes for a Rectangle
        """
        rectangle = Rectangle.create(id=1, width=2, height=3, x=4, y=5)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)

    def test_create_square(self):
        """
        Test create method with a dictionary of attributes for a Square
        """
        square = Square.create(id=1, size=2, x=3, y=4)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_to_json_string_multiple_dictionaries(self):
        """
        Test to_json_string method with multiple dictionaries
        """
        self.assertEqual(Base.to_json_string(
            [{'id': 12}, {'id': 13}]), '[{"id": 12}, {"id": 13}]')

    def test_from_json_string_multiple_dictionaries(self):
        """
        Test from_json_string method with multiple dictionaries
        """
        self.assertEqual(Base.from_json_string('[{"id": 12}, {"id": 13}]'),
                         [{'id': 12}, {'id': 13}])

    def test_id_none(self):
        """Sending no id"""
        b = Base()
        self.assertEqual(1, b.id)

    def test_id_zero(self):
        """Sending an id 0"""
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        """Sending a negative id"""
        b = Base(-20)
        self.assertEqual(-20, b.id)

    def test_id_string(self):
        """Sending an id that is not an int"""
        b = Base("Betty")
        self.assertEqual("Betty", b.id)

    def test_id_list(self):
        """Sending an id that is not an int"""
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_dict(self):
        """Sending an id that is not an int"""
        b = Base({"id": 109})
        self.assertEqual({"id": 109}, b.id)

    def test_to_json_type(self):
        """Testing the json string"""
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        """Testing the json string"""
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(
            json.loads(json_string), [{"id": 609, "y": 0, "size": 1, "x": 0}]
        )

    def test_to_json_None(self):
        """Testing the json string"""
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        """Testing the json string"""
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")


if __name__ == '__main__':
    unittest.main()
