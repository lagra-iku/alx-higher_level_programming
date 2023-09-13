#!/usr/bin/python3
"""
Exact same object
"""


def is_same_class(obj, a_class):
    """
    a function that returns True if the object is
    exactly an instance of the specified class;
    otherwise False
    Args:
        obj: object to check
        a_class: class to compare to
    """
    if type(obj) is a_class:
        return (True)
    return (False)
