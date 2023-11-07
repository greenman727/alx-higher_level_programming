#!/usr/bin/python3
"""Defines an class BaseGeometry"""


class BaseGeometry:
    """Defines a base geometry."""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a parameter as an integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise TypeError(f"{name} must be greater than 0")
