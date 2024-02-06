#!/usr/bin/python3

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

    # Replace the specified characters with themselves followed by a newline character
    for char in [".", "?", ":"]:
        text = text.replace(char, char + "\n")

    # Split the text into lines and strip leading and trailing spaces from each line
    lines = text.split("\n")
    for i, line in enumerate(lines):
        print(line.strip(), end="")
        if i < len(lines) - 1:
            print("\n")
