#!/usr/bin/python3
"""
This is the base class
"""
import json


class Base:
    """
    This is the base of other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a private instance attr
        Args:
          id (int): Public id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file:"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                json_serialize = [i.to_dictionary() for i in list_objs]
                json_data = cls.to_json_string(json_serialize)
                file.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
