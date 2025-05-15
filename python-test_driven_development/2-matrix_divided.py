#!/usr/bin/python3
"""
Function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of the matrix by div.

    Args:
        matrix (list of lists of int/float): matrix to divide
        div (int or float): divisor

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats,
                   or if rows are not all the same size,
                   or if div is not a number
        ZeroDivisionError: if div is 0

    Returns:
        new matrix (list of lists) with all elements divided by div,
        rounded to 2 decimal places
    """
    if (not isinstance(matrix, list) or
        any(not isinstance(row, list) for row in matrix) or
        any(not all(isinstance(el, (int, float)) for el in row)
            for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    row_length = len(matrix[0]) if matrix else 0
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
