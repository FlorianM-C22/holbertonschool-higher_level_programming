#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Prints all integers of a list.

    Parameters:
    - my_list: A list of integers

    Returns:
    int:  An integer per line

    """

    for i in my_list:
        print("{:d}".format(i))
