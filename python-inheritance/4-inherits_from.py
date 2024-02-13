#!/usr/bin/python3
"""
Module for inherits_from function.
"
"
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited from
    the specified class; otherwise False.

    Args:
        obj: The object to inspect.
        a_class: The class to compare the object with.

    Returns:
        True if the object is an instance of a class that inherited from
        the specified class; otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
