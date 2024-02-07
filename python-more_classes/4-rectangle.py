#!/usr/bin/python3
class Rectangle:
    """
    A class that defines a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle.

        """
        if not type(height) == int:
            raise TypeError("height must be an integer")
        if int(height) < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        if not type(width) == int:
            raise TypeError("width must be an integer")
        if int(width) < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
        Getter for the height of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.

        """
        if not type(value) == int:
            raise TypeError("height must be an integer")
        if int(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Getter for the width of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle.

        """
        if not type(value) == int:
            raise TypeError("width must be an integer")
        if int(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        Returns the area of the rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def print(self):
        """
        Prints the rectangle with the character '#'.
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __str__(self):
        return self.print()

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
