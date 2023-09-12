#!/usr/bin/python3
"""
to json string
"""

import json


def to_json_string(my_obj):
    """
    a funct that returns the JSON representation of an object (string)
    Args:
        my_obj : json object
    """
    return json.dumps(my_obj)
