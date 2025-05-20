#!/usr/bin/python3
"""Defines a class Square with size validation."""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): Size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
