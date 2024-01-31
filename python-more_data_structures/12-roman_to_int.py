#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Parameters:
    - roman_string: A roman numeral string

    Returns:
    - The roman numeral string converted to an integer
        or
    - 0 if roman_string is not a string or is None

    """

    if roman_string is None:
        return 0
    if type(roman_string) is not str:
        return 0

    rom_int = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    value = 0
    prev = 0
    for r in roman_string:
        if prev < rom_int.get(r):
            value += (rom_int.get(r) - 2 * prev)
        else:
            value += rom_int.get(r)
        prev = rom_int.get(r)

    return value
