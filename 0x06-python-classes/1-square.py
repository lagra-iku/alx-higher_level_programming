#!/usr/bin/python3
"""Defines class square"""


class Square:
    """defining the square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, value):
        """Initializes a private instance attr
        Args:
            value (int): length of a side of the square
        Returns: None
        """
        self.__size = value
