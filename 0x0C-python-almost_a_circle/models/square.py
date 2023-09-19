#!/usr/bin/python3
"""
A square class that inherits from the rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class square
    """

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

    def update(self, *args, **kwargs):
        """
        update the class square
        """
        fmt = ['id', 'width', 'x', 'y']
        if args is not None and len(args) != 0:
            count = 0
            for i in args:
                if count < 5:
                    setattr(self, fmt[count], i)
                    count += 1
        else:
            for key, value in kwargs.items():
                for i in fmt:
                    if (i == key):
                        setattr(self, key, value)
                if key == 'size':
                    setattr(self, 'width', value)

    def to_dictionary(self):
        """creating a dictionary representation"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
