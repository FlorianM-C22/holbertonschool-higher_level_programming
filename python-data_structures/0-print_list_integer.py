#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Prints all integers of a list.

    Parameters:
    - my_list: A list of integers

    Returns:
    int:  An integer per line

    """

    for i in range(len(my_list)):
        print("{}".format(my_list[i]))
