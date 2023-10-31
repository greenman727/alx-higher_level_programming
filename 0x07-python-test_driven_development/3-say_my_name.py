#!/usr/bin/python3
"""Defines a function to print name"""


def say_my_name(first_name, last_name=""):
    """prints a name followed by first name and an optional last_name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
