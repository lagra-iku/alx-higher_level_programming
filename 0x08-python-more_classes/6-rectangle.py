#!/usr/bin/python3
"""
Class for a simple rectangle
"""


class Rectangle:
    """class to represent a rectangle"""
    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        print the rectangle with the character #

        Returns:
            rectangle printed with #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            string = ""
            for i in range(self.height):
                for j in range(self.width):
                    string = string + "#"
                if (i < self.height - 1):
                    string = string + "\n"
            return string

    def __repr__(self):
        """
        create a new instance of a rectangle

        Returns:
            rectangle printed with #
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        deletes an instance of a rectangle

        Returns:
            none
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
