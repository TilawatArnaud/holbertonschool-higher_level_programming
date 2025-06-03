#!/usr/bin/python3
"""
Module for from_json_string
"""


def from_json_string(my_str):
    """
    Function that returns the JSON representation of an object (string).
    """
    import json
    return json.loads(my_str)
