#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).

    Parameters:
    - my_list: a list of integers

    Returns:
    The sum of all unique integers

    """

    uniques = set(my_list)
    result = sum(uniques)

    return result
