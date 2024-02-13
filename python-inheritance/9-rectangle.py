#!/usr/bin/python3
"""
Module for Rectangle class inherited from BaseGeometry.
"
"
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes the Rectangle.

        Args:
            width: The width of the Rectangle.
            height: The height of the Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
