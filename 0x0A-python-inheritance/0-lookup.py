#!/usr/bin/python3
"""Defines a function that returns the list of available attributes"""


def lookup(obj):
    """Returns a list of available attributes of an Object"""
    return (dir(obj))
