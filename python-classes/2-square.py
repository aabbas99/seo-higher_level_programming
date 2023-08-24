#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a Square."""

    def __init__(self, size = 0):
        """Initalize a new Square.

        Args:
            size(int) The size of the new square.
        """

        if size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        self.__size = size
