#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides 2 integers and prints the result.

    Parameters:
    - a: integer 1
    - b: integer 2

    Returns:
    - The value of the division
        otherwise
    - None

    """

    result = None

    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
