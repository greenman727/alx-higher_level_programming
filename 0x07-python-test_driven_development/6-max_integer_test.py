#!/usr/bin/python3
"""Defines a function to find the max integer"""


def max_integer(list=[]):
    """A function to find the max integer in a list of integers"""
    if len(list) == 0:
        return None
    result = list[0]
    a = 1
    while a < len(list):
        if list[a] > result:
            result = list[a]
        a += 1
    return result
