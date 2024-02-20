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
        r1 = rectangle(5, 10, id=1)
        self.assertEqual(r1.id, 1)
        r2 = rectangle(5, 10, id=2)
        self.assertEqual(r2.id, 2)
        r3 = rectangle(5, 10, id=12)
        self.assertEqual(r3.id, 12)
        r4 = rectangle(5, 10, id=3)
        self.assertEqual(r4.id, 3)

    def test_to_json_string(self):
        """
        Test to_json_string
        """
        r1 = rectangle(5, 10)
        self.assertEqual(r1.to_json_string(None), "[]")
        self.assertEqual(r1.to_json_string([]), "[]")
        self.assertEqual(r1.to_json_string([{'id': 89}]), '[{"id": 89}]')
        self.assertEqual(r1.to_json_string([{'id': 89}, {'id': 89}]),
                         '[{"id": 89}, {"id": 89}]')

    def test_from_json_string(self):
        """
        Test from_json_string
        """
        r1 = rectangle(5, 10)
        self.assertEqual(r1.from_json_string(None), [])
        self.assertEqual(r1.from_json_string("[]"), [])
        self.assertEqual(r1.from_json_string('[{"id": 89}]'), [{'id': 89}])
        self.assertEqual(r1.from_json_string('[{"id": 89}, {"id": 89}]'),
                         [{'id': 89}, {'id': 89}])

    def test_save_to_file(self):
        """
        Test save_to_file
        """
        r1 = rectangle(5, 10)
        r1.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_width(self):
        """
        Test width
        """
        r1 = rectangle(5, 10)
        self.assertEqual(r1.width, 5)
        r1.width = 15
        self.assertEqual(r1.width, 15)
        with self.assertRaises(TypeError):
            r1.width = "invalid"
        with self.assertRaises(ValueError):
            r1.width = -5

    def test_height(self):
        """
        Test height
        """
        r1 = rectangle(5, 10)
        self.assertEqual(r1.height, 10)
        r1.height = 20
        self.assertEqual(r1.height, 20)
        with self.assertRaises(TypeError):
            r1.height = "invalid"
        with self.assertRaises(ValueError):
            r1.height = -10

    def test_x(self):
        """
        Test x
        """
        r1 = rectangle(5, 10, 2)
        self.assertEqual(r1.x, 2)
        r1.x = 5
        self.assertEqual(r1.x, 5)
        with self.assertRaises(TypeError):
            r1.x = "invalid"
        with self.assertRaises(ValueError):
            r1.x = -2

    def test_y(self):
        """
        Test y
        """
        r1 = rectangle(5, 10, 2, 3)
        self.assertEqual(r1.y, 3)
        r1.y = 6
        self.assertEqual(r1.y, 6)
        with self.assertRaises(TypeError):
            r1.y = "invalid"
        with self.assertRaises(ValueError):
            r1.y = -3

    def test_area(self):
        """
        Test area
        """
        r1 = rectangle(5, 10)
        self.assertEqual(r1.area(), 50)
        r2 = rectangle(3, 7)
        self.assertEqual(r2.area(), 21)

    def test_str(self):
        """
        Test __str__
        """
        r1 = rectangle(5, 10, 2, 3, 1)
        expected_output = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(r1), expected_output)

    def test_update(self):
        """
        Test update
        """
        r1 = rectangle(5, 10, 2, 3, 1)
        r1.update(10)
        self.assertEqual(r1.id, 10)
        r1.update(10, 20)
        self.assertEqual(r1.width, 20)
        r1.update(10, 20, 30)
        self.assertEqual(r1.height, 30)
        r1.update(10, 20, 30, 40)
        self.assertEqual(r1.x, 40)
        r1.update(10, 20, 30, 40, 50)
        self.assertEqual(r1.y, 50)
        r1.update(id=20)
        self.assertEqual(r1.id, 20)
        r1.update(width=30)
        self.assertEqual(r1.width, 30)
        r1.update(height=40)
        self.assertEqual(r1.height, 40)
        r1.update(x=50)
        self.assertEqual(r1.x, 50)
        r1.update(y=60)
        self.assertEqual(r1.y, 60)

    def test_to_dictionary(self):
        """
        Test to_dictionary
        """
        r1 = rectangle(5, 10, 2, 3, 1)
        expected_output = {'x': 2, 'y': 3, 'id': 1, 'height': 10, 'width': 5}
        self.assertEqual(r1.to_dictionary(), expected_output)


if __name__ == '__main__':
    unittest.main()
