#!/usr/bin/python3
"""Defines a class Square with size, position, area, and print."""


class Square:
    """Class that defines a square with size, position, area, and printing."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' character and the position offset."""
        if self.__size == 0:
            print()
            return

        # Print newlines for vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print each line of the square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
