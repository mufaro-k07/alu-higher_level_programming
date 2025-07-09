#!/usr/bin/python3
"""
This module defines a class Square with a private size attribute.
"""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size: The size of the square (no type/value validation).
        """
        self.__size = size
