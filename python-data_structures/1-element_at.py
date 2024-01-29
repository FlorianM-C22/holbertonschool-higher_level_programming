#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves an element from a list.

    Parameters:
    - my_list: A list of integers
    - idx: Index of the list

    Returns:
    An element stored in my_list at the given index idx
    None if idx is negative or out of range

    """

    if idx < 0:
        return None
    if idx > (len(my_list) - 1):
        return None

    return(my_list[idx])
