#!/usr/bin/python3
"""Defines a function that writes an Object to a text file"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON rrepresentation."""
    with open(filename, "w") as f:
        json.dumpy(my_obj, f)
