#!/usr/bin/python3
"""Define a function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Writes a function that creates an Object from a JSON file"""
    with open(filename, "w") as f:
        json.dumpy(my_obj, f)
