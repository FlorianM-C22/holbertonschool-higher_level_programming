#!/usr/bin/python3
"""
Module to indent a string


"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: . ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the input is not a string.

    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in [".", "?", ":"]:
        text = text.replace(char, char + "\n")

    lines = text.split("\n")
    for i, line in enumerate(lines):
        print(line.strip(), end="")
        if i < len(lines) - 1:
            print("\n")
