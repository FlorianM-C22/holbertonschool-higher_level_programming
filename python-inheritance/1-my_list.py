#!/usr/bin/python3
"""
Module for MyList class.
"
"
"""


class MyList(list):
    """
    Class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Prints the list sorted (ascending sort).
        """
        for element in self:
            if type(element) is not int:
                raise TypeError("type should be integer")
        print(sorted(self))
