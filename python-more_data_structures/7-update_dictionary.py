#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Prints a dictionary by ordered keys.

    Parameters:
    - a_dictionary: A dictionary
    - key: Key of a value
    - value: Value

    Returns:
    - The sorted dictionary

    """

    if value or key in a_dictionary.copy:
        a_dictionary.update({key: value})
    else:
        a_dictionary.append({key: value})

    return a_dictionary
