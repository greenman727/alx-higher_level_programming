#!/usr/bin/python3
"""Defines a class that inherits from int"""


class MyInt(int):
    """Inverts int operators"""

    def __eq__(self, value):
        """Override operators"""
        return self.real != value

    def __ne__(self, value):
        """Override Operators"""
        return self.real == value
