#!/usr/bin/python3
"""Defines class square"""


class Square:
    """defining the square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """
        Initializes a private instance attr
        Args:
            value (int): length of a side of the square
        Raises:
            TypeError: checks if size is not integer
            ValueError: checks if size is < 0
        Returns:
            None
        """
        if not type(size) == int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """
        Calculates the current square area
        Returns:
            area of square
        """
        return self.__size ** 2
