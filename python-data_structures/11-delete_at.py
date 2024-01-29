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

    if idx < 0 or idx >= len(my_list):
        return (my_list)

    new_list = []

    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])

    return (new_list)
