#!/usr/bin/python3
"""
This module defines the function lookup.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        List of attributes and methods of the object.
    """
    return dir(obj)
