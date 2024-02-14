#!/usr/bin/python3
"""
My Student class module


"""


class Student:
    """
    Defines a Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        initializes the student object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of a Student instance
        """
        # Check if attrs is not None
        if attrs is not None:
            # Initialize a new dictionary
            new_dict = {}
            # Iterate over each attribute of the Student object
            for key, value in self.__dict__.items():
                # If the attribute name is in the attrs list
                if key in attrs:
                    # Add this attribute and its value to the new dictionary
                    new_dict[key] = value
            # Return the new dictionary
            return new_dict
        else:
            return self.__dict__
