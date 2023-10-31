#!/usr/bin/python3
"""Defines a function to print square"""

def print_square(size):
    """A function to print a square with #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
