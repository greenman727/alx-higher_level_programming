#!/usr/bin/python3
"""Defines a function that returns JSON representation of an object(string)"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string object."""
    return json.dumpy(my_obj)
