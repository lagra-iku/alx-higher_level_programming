#!/usr/bin/python3
"""
My List
"""


class MyList(list):
    """
    a class MyList that inherits from list
    """

    def print_sorted(self):
        """
        prints the list but sorted
        """
        print(sorted(self))
