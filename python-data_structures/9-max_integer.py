#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list.

    Parameters:
    - my_list: A list of integers

    Returns:
    - The biggest integer of my_list

    """

    if not my_list:
        return (None)

    my_list.sort()

    return (my_list[-1])
