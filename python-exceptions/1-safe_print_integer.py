#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().

    Parameters:
    - value: can be any type (integer, string, etc.)

    Returns:
    - True: value has been correctly printed (it means the value is an integer)
        otherwise
    - False

    """

    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
