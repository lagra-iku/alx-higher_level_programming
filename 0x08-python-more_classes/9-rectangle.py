#!/usr/bin/python3
"""
Class for a simple rectangle
"""


class Rectangle:
    """class to represent a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

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
                    string = string + str(self.print_symbol)
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        Args:
            rect_1: rectangle 1.
            rect_2: rectangle 2.
        Raises:
            TypeError: if not an instance of a Rectangle
        Returns:
            The rectangle with the biggest area
            or rectangle 1 if they have the same area
        """
        if not type(rect_1) == Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not type(rect_2) == Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with
        width == height == size
        Args:
            size (int): The size of the rectangle. Defaults to 0.
        Returns:
            Rectangle: A new Rectangle instance with
            width and height equal to size.
        """
        return cls(size, size)
