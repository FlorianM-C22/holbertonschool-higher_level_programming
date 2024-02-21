#!/usr/bin/python3
"""
Unittest for Square class


"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test cases for Square class
    """

    def test_constructor(self):
        """
        Test the constructor of Square class
        """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertIsNotNone(s1.id)

        s2 = Square(10, 2, 3, 1)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 1)

    def test_str(self):
        """
        Test the __str__ method of Square class
        """
        s = Square(5, 2, 3, 1)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 5")

    def test_size_getter_setter(self):
        """
        Test the size getter and setter of Square class
        """
        s = Square(5)
        self.assertEqual(s.size, 5)

        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_update_args(self):
        """
        Test the update method of Square class with *args
        """
        s = Square(5)
        s.update(1, 10, 2, 3)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_update_kwargs(self):
        """
        Test the update method of Square class with **kwargs
        """
        s = Square(5)
        s.update(id=1, size=10, x=2, y=3)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method of Square class
        """
        s = Square(5, 2, 3, 1)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 1, "x": 2, "size": 5, "y": 3})


if __name__ == '__main__':
    unittest.main()
