#!/usr/bin/python3
def print_last_digit(number):
    """
    Prints the last digit of a number.

    Parameters:
    - number (int): The number entered

    Returns:
    int:  The value of the last digit

    """

    last_digit = abs(number) % 10
    print(last_digit, end='')
    return last_digit
