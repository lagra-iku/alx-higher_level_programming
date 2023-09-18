#!/usr/bin/python3
"""
This is the base class
"""


class Base:
    """
    This is the base of other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a private instance attr
        Args:
          id (int): Public id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
