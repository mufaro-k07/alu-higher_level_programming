#!/usr/bin/python3
"""
Module: 11-student

This module defines a Student class that supports both serialization
(to a dictionary) and deserialization (updating from a dictionary).

Author: ALU Higher Level Programming
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        If attrs is a list of strings, returns only the attributes listed
        and present in the instance. Otherwise, returns all attributes.

        Args:
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: A dictionary of the requested student attributes.
        """
        if isinstance(attrs, list) and all(
            isinstance(attr, str) for attr in attrs
        ):
            return {
                key: getattr(self, key)
                for key in attrs if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        using the provided dictionary.

        Args:
            json (dict): Dictionary with new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
