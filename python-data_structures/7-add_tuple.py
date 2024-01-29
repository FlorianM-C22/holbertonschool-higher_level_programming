#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds 2 tuples.

    Parameters:
    - tuple_a: Tuple with an integer
    - tuple_b: Tuple with an integer

    Returns:
    A tuple with 2 integers :
    - The 1st element is the addition of the first element of each argument
    - The 2nd element is the addition of the second element of each argument

    """

    result_tuple = ()

    element_a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    element_a2 = tuple_a[1] if len(tuple_a) >= 2 else 0

    element_b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    element_b2 = tuple_b[1] if len(tuple_b) >= 2 else 0

    result_tuple = (element_a1 + element_b1, element_a2 + element_b2)

    return result_tuple
