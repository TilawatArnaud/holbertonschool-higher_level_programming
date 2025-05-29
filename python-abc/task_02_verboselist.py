#!/usr/bin/env python3
"""
This module defines a custom list class, VerboseList,
which extends Python's built-in list with verbose notifications
for common list operations like append, extend, remove, and pop.
"""


class VerboseList(list):
    """
    A custom list class that prints notifications when items
    are added or removed using append, extend, remove, or pop.
    """

    def append(self, item):
        """
        Append an item to the list and print a notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list by appending elements from the iterable
        and print a notification.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of item from the list
        and print a notification.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return the item at the given index (default last).
        Print a notification before popping the item.
        """
        item = self[index]  # Save item before popping
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
