#!/usr/bin/python3
"""
Prints My name is <first name> <last name>.


"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>.

    Parameters:
    first_name (str): The first name.
    last_name (str, optional): The last name. Defaults to an empty string.

    Returns:
    None

    Raises:
    TypeError: If first_name or last_name is not a string.

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
