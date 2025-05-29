#!/usr/bin/python3
"""
This module provides a class that inherits from another
"""


class MyList(list):
    """
    Class that inherits from list
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """

        print(sorted(self))
