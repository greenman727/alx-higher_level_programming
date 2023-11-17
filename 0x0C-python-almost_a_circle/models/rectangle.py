#!/usr/bin/python3
"""Defines a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Defines a class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Inializes a class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the size of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if type(height) is notint:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets of x variable"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x variable"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >+ 0")
        self.__x = value

    @property
    def y(self):
        """Gets of y variable"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets of y variable"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise valuError("y must >+ 0")
        self.__y = value

    def area(self):
        """Sets an area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Defines an area of the rectangle"""
        for a in range(self.y):
            print()
        for a in range(self.height):
            print(" " * self.x + self.width * '#')

    def __str__(self):
        """Defines a string method"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """Defines arguments"""
        dict_order = ['id', 'width', 'height', 'x', 'y']
        if args is not None and bool(args) is True:
            i = 0
            for key in dict_order:
                try:
                    setattr(self, key, args[i])
                except IndexError:
                    pass
                i += 1
        else:
            for key in dict_order:
                try:
                    setattr(self, key, kwargs[key])
                except keyError:
                    pass

        def to_dictionary(self):
            """Returns the dictionary representation of a Rectangle"""
            dict_order = ['x', 'y', 'id', 'height', 'width']
            dict_attrs = {}
            for key in dict_order:
                dict_attrs[key] = getattr(self, key)
            return dict_attrs
