#!/usr/bin/python3
"""Contains a class definition of 'Square'"""


class Square():
    """Definition of private size in Square"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
