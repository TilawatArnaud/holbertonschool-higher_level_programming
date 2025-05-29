#!/usr/bin/python3
"""
Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, which is a special kind of rectangle.

    Attributes:
        __size (int): The size of the square's sides (private).
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square sides.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is <= 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: Area (size * size)
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: The square description [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
