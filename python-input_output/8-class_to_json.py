#!/usr/bin/python3
"""
Module for class_to_json
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of
    an object.

    Args:
        obj: An instance of a class with serializable attributes

    Returns:
        dict: A dictionary containing all serializable attributes of the object
    """
    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (int, str, bool, list, dict)):
            result[key] = value
        elif key.startswith('_') and not key.startswith('__'):
            result[key] = value
    return result
