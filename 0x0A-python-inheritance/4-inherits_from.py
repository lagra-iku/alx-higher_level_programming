#!/usr/bin/python3
"""
Only subclass of
"""


def is_kind_of_class(obj, a_class):
    """
    Write a function that returns True if the object
    is an instance of a class that inherited
    (directly or indirectly) from the specified class;
    otherwise False.
    Args:
        obj: object to check
        a_class: class to compare to
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
