#!/usr/bin/env python3
"""
Defines an abstract Animal class and its concrete subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for all animals.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that should return the sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal.
    """

    def sound(self):
        """
        Returns the sound a dog makes.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal.
    """

    def sound(self):
        """
        Returns the sound a cat makes.
        """
        return "Meow"
