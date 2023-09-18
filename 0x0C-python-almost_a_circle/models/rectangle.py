#!/usr/bin/python3
"""A Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """class to represent a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
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
        self.x = x
        self.y = y
        super().__init__(id)

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
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Retrieve x property
        Returns:
            x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set x property
        Args:
            value (int): x
        Returns:
            None
        """
        if not type(value) == int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Retrieve y property
        Returns:
            y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set y property
        Args:
            value (int): y
        Returns:
            y
        """
        if not type(value) == int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
