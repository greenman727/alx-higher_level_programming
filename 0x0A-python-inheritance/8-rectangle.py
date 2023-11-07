#!/usr/bin/python3
"""Defines a class Rectangle that inherits BaseGeometry properties"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class BaseGeometry(BaseGeometry):
    """Defines a base geometry."""

    def __init__(self, width, height):
        """Initializes a class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
