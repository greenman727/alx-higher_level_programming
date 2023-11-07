#!/usr/bin/python3
"""Defines a square that inherits from a class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a square"""

    def __init__(self, size):
        """Initializes a square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
