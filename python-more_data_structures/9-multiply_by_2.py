#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2

    Parameters:
    - a_dictionary: A dictionary

    Returns:
    - New dictionary with the values multiplied by 2

    """

    new_dictionary = a_dictionary.copy()

    for value in new_dictionary:
        new_dictionary[value] *= 2

    return new_dictionary
