#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """A class to define a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initailizes the rectangle"""
        self.height = height
        self.width = width

        @property
        def width(self):
            """set the width of the resctangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """sets the width of the rectangle"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """set the height of the rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
