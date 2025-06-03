#!/usr/bin/python3
"""
Function for write a filetext
"""

def write_file(filename="", text=""):
    """
    Function for write a filetext
    """
    with open(filename, "w", encoding="UTF-8") as the_file:
        the_file.write(text)
    return len(text)
