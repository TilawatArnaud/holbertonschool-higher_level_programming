#!/usr/bin/python3
"""
Module that defines the BaseGeometry class,
a base class for geometric shapes.
"""


class BaseGeometry:
    """
    Base class for geometric shapes.

    This class is designed to be a base class
    for different geometric shapes and will be
    extended by child classes.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        This method must be implemented by child classes.

        Raises:
            Exception: This method is not implemented
            in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that the value is a positive integer.

        Args:
            name (str): The name of the value to validate
            value: The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
