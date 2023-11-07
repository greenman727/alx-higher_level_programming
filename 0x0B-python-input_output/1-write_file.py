#!/usr/bin/python3
"""Defines a function to write a file"""


def write_file(filename="", text=""):
    """Writes a string to a UTFB text fille."""
    with open(filename, "W", encoding="utf-8"i) as f:
        return f.write(text)
