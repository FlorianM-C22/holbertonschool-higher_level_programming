#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds 2 integers.

    Parameters:
    - a: 1st integer
    - b: 2nd integer

    Returns:
    - The sum of integer a + b

    Raises:
    - TypeError: If either a or b is not an integer

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
