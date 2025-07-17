#!/usr/bin/python3
"""
This module provides a function that writes a Python object
to a text file using its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """Writes a Python object to a text file using JSON format.

    Args:
        my_obj: The object to serialize.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
