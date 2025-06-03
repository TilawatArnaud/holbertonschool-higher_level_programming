#!/usr/bin/python3
"""
    Modules for append write
"""


def append_write(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns character count.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        chars_written = f.write(text)
    return chars_written
