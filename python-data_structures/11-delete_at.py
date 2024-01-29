#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Parameters:
    - my_list: A list of integers
    - idx: The position of the item to delete

    Returns:
    - A new list with the deleted item
        or
    - The same list if idx is negative or out of range

    """

    if not idx < 0 and not idx >= len(my_list):
        del my_list[idx]

    return my_list
