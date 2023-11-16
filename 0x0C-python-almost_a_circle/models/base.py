#!/usr/bin/python3
"""Defines a class Base"""
import json
import csv
from collections import OrderedDict
import turtle


class Base:
    """Defines a class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns theJSON serialization of a dcitionary"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """returns the json serialiization"""
        filename = cls___name__ + ".json"
        with open(filename, "w") as fl:
            if list_objs is None:
                fl.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                fl.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the deserialized JSON string."""
        if json_string is None or json_string == "{}":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns a class intances"""
        if dictionary and dictionary != {}:
            if clas.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of classes intantiated"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as fl:
                list_dicts = Base.from_json_string(fl.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes a csv serialization"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfl:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldname = ["id", "size", "x", "y"]
                writer = csv.Dictwriter(csvfile, filenames=fieldnmae)
                for obj in list_objs:
                    writer.writerow(obj.to.dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of classes instantiated."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfl:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfl, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
