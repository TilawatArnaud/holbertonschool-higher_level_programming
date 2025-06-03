#!/usr/bin/python3
"""
Module for Student class
"""


class Student:
    """
    Class for Student
    """
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """
        Initialize the Student object with first name, last name, and age.

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object.

        Args:
            obj: An instance of a class with serializable attributes

        Returns:
            A dictionary containing all serializable attributes of the object
        """
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (int, str, bool, list, dict)):
                result[key] = value
            elif key.startswith('_') and not key.startswith('__'):
                result[key] = value
        return result
