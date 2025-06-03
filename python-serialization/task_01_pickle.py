#!/usr/bin/python3
"""
Module for demonstrating object serialization using pickle.
"""

import pickle
import os


class CustomObject:
    """
    A custom class that demonstrates serialization using pickle.
    """
    def __init__(self, name="", age=0, is_student=False):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the person
            age (int): The age of the person
            is_student (bool): Whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object to a file using pickle.

        Args:
            filename (str): The name of the file to save the serialized object

        Returns:
            int: 1 if successful, None otherwise
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            return 1
        except (pickle.PicklingError, IOError, AttributeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        Args:
            filename (str): The name of the file to load the serialized object

        Returns:
            CustomObject: The deserialized object
            None if deserialization fails
        """
        try:
            if not os.path.exists(filename):
                return None
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (pickle.UnpicklingError, AttributeError, EOFError, IOError):
            return None
