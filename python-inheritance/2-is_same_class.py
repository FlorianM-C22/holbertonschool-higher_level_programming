#!/usr/bin/python3
"""
Module for is_same_class function.
"
"
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise False.

    Args:
        obj: The object to inspect.
        a_class: The class to compare the object with.

    Returns:
        True if the object is exactly an instance of the specified class;
        otherwise False.
    """
    if type(obj) is not a_class:
        return False
    else:
        return True
