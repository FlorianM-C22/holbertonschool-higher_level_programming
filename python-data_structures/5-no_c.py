#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all characters c and C from a string.

    Parameters:
    - my_string: A string of characters

    Returns:
    The new string

    """

    return (my_string.translate({ord(i): None for i in 'cC'}))
