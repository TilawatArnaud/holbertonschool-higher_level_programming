#!/usr/bin/python3
"""
Module for load_from_json_file
"""


def load_from_json_file(filename):
    """
    Function that creates an Object from a "JSON file".
    """
    import json
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
