#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Parameters:
    - matrix: a list of integers or floats
    - div: an integer or float used to divide with

    Returns:
    - The elements of 'matrix' divided by 'div'

    Raises:
    - TypeError: If matrix is not a list of int or floats
    - TypeError: If each row of matrix is not of the same size
    - TypeError: If div is not an int or a float
    - ZeroDivisionError: If div is 0

    """

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix
