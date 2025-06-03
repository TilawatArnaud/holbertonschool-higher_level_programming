#!/usr/bin/python3
"""
Basic serialization module that converts between Python dictionaries and JSON files.
"""

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data: A Python Dictionary with data to be serialized
        filename: The filename of the output JSON file
    """
    import json
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file to a Python dictionary.

    Args:
        filename: The filename of the input JSON file

    Returns:
        dict: A Python Dictionary with the deserialized JSON data
    """
    import json
    with open(filename, 'r') as f:
        return json.load(f)
