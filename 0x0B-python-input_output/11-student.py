#!/usr/bin/python3
"""
Student to disk and reload
"""


class Student:
    """
    a class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if type(attrs) is not list:
            return (self.__dict__)
        else:
            new_list = {}
            obj = self.__dict__
            for i in attrs:
                for item in obj:
                    if (i == item):
                        new_list[i] = obj[i]
            return (new_list)

    def reload_from_json(self, json):
        """
        that replaces all attributes of the Student instance
        Args:
            json: json
        """
        obj = self.__dict__
        for i in json:
            for item in obj:
                if (item == i):
                    setattr(self, i, json[i]}
