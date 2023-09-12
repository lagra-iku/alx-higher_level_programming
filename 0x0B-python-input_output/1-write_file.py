#!/usr/bin/python3
"""
write to file
"""


def write_file(filename="", text=""):
    """
    a funct that writes a string to a text file (UTF8)
    Args:
        filename (str): file name
        txt (str): text to write to file
    Returns:
        the number of characters written
    """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
