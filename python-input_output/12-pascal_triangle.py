#!/usr/bin/python3
"""
This module contains a function that returns a list of integers representing
Pascal's triangle of n:

"""


def pascal_triangle(n):
    """
    Returns a list of integers representing Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        line = [1]
        for i in range(1, len(triangle[-1])):
            line.append(triangle[-1][i - 1] + triangle[-1][i])
        line.append(1)
        triangle.append(line)

    return triangle
