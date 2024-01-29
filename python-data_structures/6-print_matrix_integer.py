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
        for num in row:
            print("{:d}".format(num), end=' ')
        print()
