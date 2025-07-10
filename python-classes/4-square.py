#!/usr/bin/python3
"""
This module defines a class Square with encapsulation, validation,
and area computation method.
"""


class Square:
    """A class that defines a square by its size with a setter and getter"""
    def __init__(self, size=0):
        """
        Initialise a new Square Instance.

        Args:
            size(int): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Get current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the current area of the square."

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
