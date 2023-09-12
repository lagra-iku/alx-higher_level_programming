#!/usr/bin/python3
"""
from json string to object
"""

import json


def from_json_string(my_str):
    """
    a funct that returns the JSON representation of an object (string)
    Args:
        my_str : json object
    """
    return json.loads(my_str)
