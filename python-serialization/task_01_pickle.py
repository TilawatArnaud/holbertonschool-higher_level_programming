#!/usr/bin/python3
"""
Module for demonstrating object serialization using pickle.
"""

import pickle


class CustomObject:
    """
    A custom class that demonstrates serialization using pickle.
    """
    def __init__(self, name, age, is_student):
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

    def serialize(self):
        """
        Serialize the object to a byte stream using pickle.

        Returns:
            bytes: The serialized object, or None if serialization fails
        """
        try:
            return pickle.dumps(self)
        except (pickle.PicklingError, AttributeError) as e:
            print(f"Serialization error: {e}")
            return None

    @classmethod
    def deserialize(cls, data):
        """
        Deserialize an object from a byte stream.

        Args:
            data (bytes): The serialized object data

        Returns:
            CustomObject: The deserialized object, or None if deserialization fails
        """
        try:
            return pickle.loads(data)
        except (pickle.UnpicklingError, AttributeError, EOFError) as e:
            print(f"Deserialization error: {e}")
            return None
