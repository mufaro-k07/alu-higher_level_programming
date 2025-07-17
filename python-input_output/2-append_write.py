#!/usr/bin/python3
"""
This module defines a function that appends a string to a text file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
        filename (str): The name of the file.
        text (str): The text to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
