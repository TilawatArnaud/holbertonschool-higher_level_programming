#!/usr/bin/python3
"""
Module for def_is_same_class
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class,
    otherwise False.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare with.

    Returns:
        bool: True if type(obj) == a_class, False otherwise.
    """
    return type(obj) is a_class
