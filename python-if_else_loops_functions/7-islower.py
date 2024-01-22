#!/usr/bin/python3
def islower(c):
    """
    Checks for lowercase character.

    Parameters:
    - c (str): The character to check

    Returns:
    bool: True if the character is a lowercase letter, False otherwise.

    """

    to_ascii = ord(c)

    if to_ascii in range(97, 123):
        return True
    else:
        return False
