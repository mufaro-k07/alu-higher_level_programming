#!/usr/bin/python3
"""
Module: 8-class_to_json

This module defines a function that returns the dictionary description
with simple data structures (list, dictionary, string, integer, and boolean)
for JSON serialization of a Python object.

The function assumes that all attributes of the object are serializable.
No external modules are imported or used.

Author: ALU Higher Level Programming
"""


def class_to_json(obj):
    """Returns the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class with only serializable attributes.

    Returns:
        dict: A dictionary containing all serializable attributes
        of the object.
    """
    return obj.__dict__
