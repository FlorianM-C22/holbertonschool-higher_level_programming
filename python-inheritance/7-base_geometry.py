#!/usr/bin/python3
"""
Module for BaseGeometry class.
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
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
