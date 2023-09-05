#!/usr/bin/python3
"""Defines class LockedClass"""


class LockedClass:
    """
    prevents user from creating new instance
    """
    __slots__ = ['first_name']

    def __init__(self):
        pass
