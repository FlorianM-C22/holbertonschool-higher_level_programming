#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Parameters:
    - matrix: A matrix of integers

    Returns:
    The matrix printed

    """

    for row in matrix:
        for i, num in enumerate(row):
            if i != 0:
                print(" ", end='')
            print("{:d}".format(num), end='')
        print()
