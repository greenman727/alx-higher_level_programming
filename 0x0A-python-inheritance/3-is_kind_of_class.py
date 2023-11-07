#!/usr/bin/python3
"""Defines a function that returns True if the object is a class"""


def is_kind_of_class(obj, a_class):
    """A function that checks for the instance of a class"""
    if isinstance(obj, a_class):
        return True
    return False
