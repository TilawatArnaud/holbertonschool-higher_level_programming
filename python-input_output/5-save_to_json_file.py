#!/bin/usr/python3
"""
Module for save_to_json_file
"""


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file, using a JSON representation.
    """
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
