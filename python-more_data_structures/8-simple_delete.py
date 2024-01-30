#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Parameters:
    - a_dictionary: A dictionary
    - key: Key of a value

    Returns:
    - New dictionary with the key deleted

    """

    try:
        del a_dictionary[key]
    except KeyError:
        pass

    return a_dictionary
