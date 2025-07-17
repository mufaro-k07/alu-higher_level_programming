#!/usr/bin/python3
"""
This module defines a function that returns a Python object
from a JSON string representation.
"""

import json


def from_json_string(my_str):
    """Returns the Python object represented by a JSON string

    Args:
        my_str (str): JSON string to be deserialized

    Returns:
        object: Python object represented by the JSON string
    """
    return json.loads(my_str)
