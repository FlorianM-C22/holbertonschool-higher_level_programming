#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list.

    Parameters:
    - my_list: A list of integers

    Returns:
    - A new list with True or False whether the integer is a multiple of 2

    """

    result_list = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)

    return (result_list)
