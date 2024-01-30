#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.

    Parameters:
    - a_dictionary: A dictionary

    Returns:
    - A key with the biggest integer value.
        or
    - None if no score found.

    """

    sortedDic = sorted(a_dictionary)
    print(sortedDic)
