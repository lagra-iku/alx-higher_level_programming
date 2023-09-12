#!/usr/bin/python3
"""
Search and update
"""


def append_after(filename="", search_string="", new_string=""):
    """
    a function that inserts a line of text to a file,
    after each line containing a specific string
    Args:
        filename (int): name of file
        search_string (int): string to search for
        new_string (str): new string to update
    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = []
        while True:
            line = f.readline()
            if line == "":
                break
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)
