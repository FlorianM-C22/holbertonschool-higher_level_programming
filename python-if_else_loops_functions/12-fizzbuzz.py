#!/usr/bin/python3
def fizzbuzz():
    """
    Prints the numbers from 1 to 100 separated by a space
    For multiples of three prints Fizz.
    For multiples of five prints Buzz.
    For numbers which are multiples of both three and five prints FizzBuzz.

    Returns:
    str:  Fizz for each multiple of 3.
    str: Buzz for each multiple of 5.
    str:  FizzBuzz for each numbers which are multiples of both 3 and 5
    int: The rest of the numbers

    """

    for i in range(101):
        if i % 3 == 0:
            print("Fizz ", end='')
        elif i % 5 == 0:
            print("Buzz ", end='')
        elif i % 3 and i % 5 == 0:
            print("FizzBuzz ", end='')
        else:
            print(f"{int(i)} ", end='')
