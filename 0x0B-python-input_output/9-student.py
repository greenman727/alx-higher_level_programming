#!/usr/bin/python3
"""Defines a class that defines a student"""


class Student:
    """REpresentation of a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrives a dictionary representation of a Student"""
        return self.__dict__
