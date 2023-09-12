#!/usr/bin/python3
"""
append to a file
"""


def append_write(filename="", text=""):
    """
    a funct that appends a string at the end of a text file (UTF8)
    Args:
        filename (str): file name
        txt (str): text to append to file
    Returns:
        the number of characters written
    """
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
