#!/usr/bin/python3
"""
save object to file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    a funct that writes an Obj to a text file, using a JSON rep
    Args:
        my_obj : json object
        filename (str): name of file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
