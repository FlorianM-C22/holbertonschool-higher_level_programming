#!/usr/bin/python3
def uppercase(str):
    """
    Prints a string in uppercase followed by a new line.

    Parameters:
    - str (str): The string to convert to uppercase

    Returns:
    str: The converted string in uppercase

    """

    ascii_values = [ord(char) for char in str]

    for i in ascii_values:
        if i in range(97, 123):
            i = i - 32
        print("{}".format(chr(i)), end='')

    print()
