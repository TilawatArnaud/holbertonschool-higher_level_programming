#!/usr/bin/env python3
"""
This module implements a geometric shape system
using abstract base classes and demonstrates the concept of duck typing in Python.

Duck typing focuses on an object's behavior rather than its class inheritance.
As long as an object implements the required methods, it is treated as the expected type.

The module contains:
- An abstract class Shape that defines the interface for geometric shapes
- Two concrete classes: Circle and Rectangle, which inherit from Shape
- A utility function shape_info that uses duck typing to interact with any shape
"""

import math
from abc import ABC, abstractmethod


def shape_info(shape):
    """
    Displays information about a geometric shape.

    This function uses duck typing and accepts any object that
    implements area() and perimeter() methods, without checking its actual type.

    Args:
        shape: Any object with area() and perimeter() methods
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))


class Shape(ABC):
    """
    Abstract base class defining the interface for all geometric shapes.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the shape's area.
        Must be implemented by all subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the shape's perimeter.
        Must be implemented by all subclasses.
        """
        pass


class Circle(Shape):
    """
    Class representing a circle, inheriting from the Shape base class.
    """

    def __init__(self, radius):
        """
        Initializes a circle with the given radius.

        Args:
            radius (float): The radius of the circle
        """
        self.radius = abs(radius)

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle (π * r²)
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle (2 * π * r)
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class representing a rectangle, inheriting from the Shape base class.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with the given width and height.

        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle (width * height)
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle (2 * (width + height))
        """
        return 2 * (self.width + self.height)
