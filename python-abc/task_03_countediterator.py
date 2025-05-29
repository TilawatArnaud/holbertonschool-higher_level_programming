#!/usr/bin/env python3
"""
This module defines CountedIterator, a custom iterator
that tracks how many items have been iterated over.
"""


class CountedIterator:
    """
    An iterator that keeps track of the number of items retrieved.

    Attributes:
        iterator (iterator): The underlying iterator.
        count (int): Number of items iterated over.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator.

        Args:
            iterable (iterable): Any iterable (like a list, tuple, etc.)
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Return the iterator itself.
        """
        return self

    def __next__(self):
        """
        Return the next item from the iterator, and increment the count.

        Raises:
            StopIteration: When there are no more items.
        """
        item = next(self.iterator)  # May raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """
        Get the number of items iterated so far.

        Returns:
            int: Number of items returned by __next__.
        """
        return self.count
