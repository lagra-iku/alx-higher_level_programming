#!/usr/bin/python3
"""Defines class square"""


class Square:
    """defining the square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a private instance attr
        Args:
            size (int): length of a side of the square
            position (tuple): the position of the square
        Returns:
            None
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Retrieve position of square
        Returns:
            None
        """
        return self.__position

    @position.setter
    def size(self, value):
        """
        Set position of square
        Args:
            value (tuple): The position of the square.
        Raises:
            TypeError: not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(val, int) for val in value) or
                any(val < 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the current square area
        Returns:
            area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints to stdout the square
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
