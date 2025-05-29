#!/usr/bin/env python3
"""
Defines Shape abstract base class and its concrete subclasses Circle and Rectangle.
Also includes a shape_info function using duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    """

    @abstractmethod
    def area(self):
        """
        Should return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Should return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle shape, defined by its radius.
    """

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    Rectangle shape, defined by its width and height.
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """
    Prints area and perimeter of a shape using duck typing.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
