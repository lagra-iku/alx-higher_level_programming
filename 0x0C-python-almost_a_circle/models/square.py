#!/usr/bin/python3
"""
A square class that inherits from the rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class square
    """
    elem = 0

    def __init__(self, size, x=0, y=0, id=None):
        """ initializes an instance of square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ return size """
        return (self.width)

    @size.setter
    def size(self, size):
        """ setting value of width and height to size"""
        self.width = size
        self.height = size

    def __str__(self):
        """updating the square instance"""
        fmt = [self.id, self.x, self.y, self.width]
        return ("[Square] ({}) {}/{} - {}".format(*fmt))
