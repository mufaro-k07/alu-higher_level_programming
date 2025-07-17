#!/usr/bin/python3
"""
Module: 9-student

This module defines a Student class with attributes for first name,
last name, and age, and provides a method to retrieve a dictionary
representation suitable for JSON serialization.

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

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary of the student's attributes.
        """
        return self.__dict__
