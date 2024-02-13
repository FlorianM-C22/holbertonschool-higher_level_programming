#!/usr/bin/python3
"""
Module for Rectangle class inherited from BaseGeometry.
"
"
"""


class BaseGeometry():
    """
    Empty Class BaseGeometry.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.

        Args:
            name: The name of the value.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


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

    def print(self):
        print("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes the Square.

        Args:
            size: The size of the Square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self._Rectangle__width, self._Rectangle__height)
