#!/usr/bin/python3
"""
create object from json file
"""

import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”
    Args:
        filename (str): name of file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
