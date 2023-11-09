#!/usr/bin/python3
"""Defines a function that add attributes to an object."""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
