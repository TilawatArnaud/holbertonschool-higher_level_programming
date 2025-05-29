#!/usr/bin/python3
"""
Module for is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or
    an instance of a subclass of a_class; otherwise False.

    Args:
        obj (any): Object to check.
        a_class (type): Class to check against.

    Returns:
        bool: True if isinstance(obj, a_class), else False.
    """
    return isinstance(obj, a_class)
