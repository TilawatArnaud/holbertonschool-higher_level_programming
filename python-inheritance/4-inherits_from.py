#!/usr/bin/python3
"""
Module for inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False.

    Args:
        obj (any): Object to check.
        a_class (type): Class to check inheritance from.

    Returns:
        bool: True if type(obj) is subclass of a_class but not exactly a_class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
