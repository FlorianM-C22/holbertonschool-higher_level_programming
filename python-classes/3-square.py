#!/usr/bin/python3
"""Contains a class definition of 'Square'"""


class Square():
    """Definition of size in square"""
    def __init__(self, size=0):
        self.size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.size * self.size)
