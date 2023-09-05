#!/usr/bin/python3
"""a module that adds two functions"""


def add_integer(a, b=98):
    """
    function that adds two interger
    Args:
        a: argument 1
        b: argument 2
    Raises:
        TypeError: checks if size is not integer
        ValueError: checks if size is < 0
    Returns:
        the addition of the arguments
    """
    if type(a) == float:
        a = int(a)
    elif not type(a) == int:
        raise TypeError("a must be an integer")
    if type(b) == float:
        b = int(b)
    elif not type(b) == int:
        raise TypeError("b must be an integer")
    return a+b
