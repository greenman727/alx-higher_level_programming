#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    A class that prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name
    """
    __slot__ = ['first_name']
