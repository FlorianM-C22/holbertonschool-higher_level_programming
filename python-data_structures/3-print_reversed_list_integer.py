#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers of a list, in reverse order.

    Parameters:
    - my_list: A list of integers

    Returns:
    The list in reverse order

    """

    for i in reversed(my_list):
        print("{:d}".format(i))
