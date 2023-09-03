#!/usr/bin/python3
"""A module to print a text with 2 new lines"""


def text_indentation(text):
    """A function to print a text with 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for i in text:
        if flag == 0:
            if i == " ":
                continue
            else:
                flag = 1
        if flag == 1:
            if i == "?" or "." or ":":
                print(i)
                print()
                flag = 0
            else:
                print(i, end="")
