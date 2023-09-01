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
        """ Initliaze a new Square.

        Args:
            size(int) the size of the new square. Default is 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zeo.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of square"""
        return (self.__size)

    @size.setter
    def size(self, size):
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

    @position.setter
    def position(self, value):
        """
        Sets the position based on the value input

        Args:
            value (tuple_: The position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of a square in type int
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the # character.

        If size is equal to 0 print an empty line.
        """
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for k in range(0, self.__position[0])]
            [print("#", end="") for j in range(self.__size)]
            print("")
