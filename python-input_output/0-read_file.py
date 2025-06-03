#!/usr/bin/python3
"""
Module for reading and printing the contents of a text file.

This module provides a function to read
and display the contents of a text file.
"""


def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The path to the file to be read.
        Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, 'r') as file:
        print(file.read(), end="")
