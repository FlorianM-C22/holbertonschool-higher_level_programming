#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Parameters:
    - matrix: A two dimensionnal array

    Returns:
    A new matrix where each value is the square of the value of the input

    """

    squares = [[0] * len(row) for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            squares[i][j] = pow(matrix[i][j], 2)

    return squares
