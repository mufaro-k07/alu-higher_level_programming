#!/usr/bin/python3
"""
This module provides a function that creates a Python object
from a JSON file.
"""

import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        The Python object represented by the JSON content.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
