#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file."""

import sys
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing items if the file exists, else start with an empty list
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all command-line arguments (excluding script name)
items.extend(sys.argv[1:])

# Save updated list back to file
save_to_json_file(items, filename)
