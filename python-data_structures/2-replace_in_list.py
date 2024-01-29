#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific position.

    Parameters:
    - my_list: A list of integers
    - idx: Index of the list
    - element: The replacement element

    Returns:
    The new list with the replacement element
    The original list if idx is negative or out of range

    """

    if idx < 0:
        return (my_list)
    if idx > (len(my_list) - 1):
        return (my_list)
    else:
        my_list[idx] = element
    return (my_list)
