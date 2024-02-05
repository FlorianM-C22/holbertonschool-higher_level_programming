#!/usr/bin/python3
"""Contains a class definition of 'Square'"""


class Square():
    """Definition of size in square"""

    def get_size(self):
        return self.__size

    def set_size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    size = property(get_size, set_size)

    def get_position(self):
        return self.__position

    def set_position(self, value):
        if type(value) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    position = property(get_position, set_position)

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end='')
                for _ in range(self.__size):
                    print("#", end='')
                print()
