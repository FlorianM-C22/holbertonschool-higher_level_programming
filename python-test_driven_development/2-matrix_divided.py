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
