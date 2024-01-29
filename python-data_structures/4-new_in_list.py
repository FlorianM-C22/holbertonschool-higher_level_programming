#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position
    without modifying the original list.

    Parameters:
    - my_list: A list of integers
    - idx: Index value
    - element: The replacement element

    Returns:
    The new list
        or
    A copy of the original list if idx is negative or out of range

    """

    if idx < 0:
        my_list = my_list.copy()
        return (my_list)
    if idx > (len(my_list) - 1):
        my_list = my_list.copy()
        return (my_list)
    else:
        my_list = my_list.copy()
        my_list[idx] = element
        return (my_list)
