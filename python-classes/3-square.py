#!/usr/bin/python3
"""
Module: square
This module defines the Square class
"""


class Square:
    """
    Represent a Square.

    Attributes:
        __size: The size of the square
    """

    def __init__(self, size=0):
        """
        Initalize a new Square.

        Args:
            size(int) The size of the new square. Default is 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of a square in type int
        """

        return self.__size ** 2
