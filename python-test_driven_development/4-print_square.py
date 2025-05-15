#!/usr/bin/python3
"""
Module 4-print_square
This module contains the function print_square
that prints a square made of '#' characters.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): size length of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
