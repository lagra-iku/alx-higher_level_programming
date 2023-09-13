#!/usr/bin/python3
"""
Same class or inherit from
"""


def is_kind_of_class(obj, a_class):
    """
    Write a function that returns True if the object
    is an instance of, or if the object is an instance
    of a class that inherited from, the specified class;
    otherwise False.
    Args:
        obj: object to check
        a_class: class to compare to
    """
    if isinstance(obj, a_class):
        return True
    return False
