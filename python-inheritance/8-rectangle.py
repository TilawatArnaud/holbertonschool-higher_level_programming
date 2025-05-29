#!/usr/bin/python3
"""
Defines the Rectangle class, which is a subclass of BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits functionality from BaseGeometry.

    Attributes:
        __width (int): private width of the rectangle
        __height (int): private height of the rectangle
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is less than or equal to zero
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
