#!/usr/bin/python3
"""Defines a function to return True if the object is an instance of class"""


def is_same_class(obj, a_class):
    """Checks an insatnce of a class"""
    if type(obj) == a_class:
        return True
    return False
