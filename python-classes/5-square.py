#!/usr/bin/python3
"""
This module defines a square with size, position, area, and printing.
"""


class Square:
    """A class that defines a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise a new Square instance.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The postion offset (default is (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the current size of the square.

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

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(n, int) for n in value) or
            not all(n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the current area of the square.

        Returns:
            int: Thea area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' using size and position."""
        if self.__size == 0:
            print()
            return

        # Print position[1] empty lines first
        for _ in range(self.__position[1]):
            print()

        # Print each row of the square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
