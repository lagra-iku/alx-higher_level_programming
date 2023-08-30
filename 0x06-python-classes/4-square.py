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
            size (int): length of a side of the square
        Returns:
            None
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieve property
        Returns:
            None
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set property
        Args:
            value (int): length of a side of the square
        Returns:
            None
        """
        if not type(value) == int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """
        Calculates the current square area
        Returns:
            area of square
        """
        return self.__size ** 2
