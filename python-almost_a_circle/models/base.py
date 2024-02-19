#!/usr/bin/python3
"""
Base model for all other models to inherit


"""


class Base:
    """
    Base class for other classes to inherit from
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the base model
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
