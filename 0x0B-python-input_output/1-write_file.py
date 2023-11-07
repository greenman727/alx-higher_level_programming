#!/usr/bin/python3
"""Defines a function to write a file"""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file. 
    Arguments:
        filename (str): The name of the file to write.
        text (str): The text fo write.
    Returns:
        The number of character written.
        """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
