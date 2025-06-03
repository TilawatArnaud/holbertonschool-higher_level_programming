#!/usr/bin/python3

def serialization_and_save_tofile(data, filename):
    """
    Serialize data to a file using JSON format.

    Args:
        data: The data to serialize
        filename (str): The name of the file to save the serialized data to
    """
    import json
    with open(filename, 'w') as f:
        json.dump(data, f)
    pass


def load_and_deserialize(filename):
    """
    Deserialize data from a file using JSON format.

    Args:
        filename (str): The name of the file to load the serialized data from

    Returns:
        The deserialized data
    """
    import json
    with open(filename, 'r') as f:
        return json.load(f)
    pass
