#!/usr/bin/python3
"""
Class for a simple rectangle
"""


class Rectangle:
    """class to represent a rectangle"""
    def __init__(self, width=0, height=0):
        """
        Initializes a private instance attr
        Args:
          width (int): width of the rectangle
          height (int): height of the rectangle
        Raises:
          TypeError: checks if width is not integer
          ValueError: checks if width is < 0
        Returns:
          None
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve width property
        Returns:
            None
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set width property
        Args:
            value (int): width of the rectangle
        Returns:
            None
        """
        if not type(value) == int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve height property
        Returns:
            None
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set height property
        Args:
            value (int): height of the rectangle
        Returns:
            None
        """
        if not type(value) == int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the current rectangle area
        Returns:
            area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the current rectangle perimeter
        Returns:
            perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
