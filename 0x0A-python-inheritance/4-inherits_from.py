#!/usr/bin/python3
"""Defines a function that checks for the instance of a class"""


def inherits_from(obj, a_class):
    """checks for theinstance of a class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
