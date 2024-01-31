#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    Returns a list with all values multiplied by a number.

    Parameters:
    - my_list: A list of integers
    - number: The multiplicator

    Returns:
    - A new list multiplied by number

    """

    new_list = list(map(lambda item: item * number, my_list))
    return new_list
