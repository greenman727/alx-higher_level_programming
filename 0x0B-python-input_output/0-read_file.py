#!/usr/bin/python3
"""Defines a function for reading file"""


def read_file(filename=""):
    """prints the contents of a UTB text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
