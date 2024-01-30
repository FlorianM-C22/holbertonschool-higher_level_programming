#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.

    Parameters:
    - a_dictionary: A dictionary

    Returns:
    - The sorted dictionary

    """

    myKeys = list(a_dictionary.keys())
    myKeys.sort()
    sorted_dict = {i: a_dictionary[i] for i in myKeys}

    for key, value in sorted_dict.items():
        print("{}: {}".format(key, value))
