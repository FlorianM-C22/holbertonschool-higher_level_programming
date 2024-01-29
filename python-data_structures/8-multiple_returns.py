#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.

    Parameters:
    - sentence: The sentence to be tested

    Returns:
    The length of a string and its first character
        or
    If the sentence is empty, the first character should be equal to None

    """

    if not sentence:
        return (len(sentence), None)
    else:
        return (len(sentence), sentence[0])
