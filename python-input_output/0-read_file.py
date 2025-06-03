#!/usr/bin/python3
"""
Module for reading and printing the contents of a text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The path to the file to be read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
