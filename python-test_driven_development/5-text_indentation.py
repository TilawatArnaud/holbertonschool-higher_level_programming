#!/usr/bin/python3
"""
Module text_indentation
Provides a function to print a text with two new lines
after each of these characters: '.', '?', and ':'.

Functions:
    text_indentation(text): Prints the text with proper indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:
    '.', '?', and ':'

    Args:
        text (str): The input text to print

    Raises:
        TypeError: If text is not a string

    Examples:
    >>> text_indentation("Hello. How are you? I'm fine:")
    Hello.

    How are you?

    I'm fine:

    >>> text_indentation(123)
    Traceback (most recent call last):
        ...
    TypeError: text must be a string

    >>> text_indentation("")

    >>> text_indentation("No spaces after colon:   But after dot.  Yes.")
    No spaces after colon:

    But after dot.

    Yes.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    while i < length:
        print(text[i], end='')

        if text[i] in {'.', '?', ':'}:
            print()  # first newline
            print()  # second newline

            i += 1
            # skip all spaces after punctuation
            while i < length and text[i] == ' ':
                i += 1
            continue

        i += 1
