#!/usr/bin/python3

class Student:
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (int, str, bool, list, dict)):
                result[key] = value
            elif key.startswith('_') and not key.startswith('__'):
                result[key] = value
        return result
