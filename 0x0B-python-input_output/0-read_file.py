#!/usr/bin/python3
"""
Read file
"""


def read_file(filename=""):
    """
    a funct that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, encoding="utf-8") as f:
        read_file = f.read()
        print(read_file, end="")
