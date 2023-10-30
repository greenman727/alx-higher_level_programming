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

        def area(self):
            """returns the area of the rectangle"""
            return self.__width * self.__height

        def perimeter(self):
            """returns the perimeter of the rectangle"""
            if self.__width == 0 or self.__height == 0:
                return 0
            return (self.__width * 2) + (self__height * 2)

        def __str__(self):
            """returns printable string representation of the rectangle"""
            if self.__width == 0 or self.height == 0:
                return("")

            if self___width != 0 and self.__height != 0:
                string += "\n".join(str(self.print_symbol) * self__width for j in range(self.__height))
                return string

        def __repr__(self):
            """returns the string representation of the Rectangle"""
            return "Rectangle({:}, {:d})".format(self.__width, self.__height)

        def __del__(self):
            """prints a message when Rectangle is deleted"""
            type(self).number_of_instances -= 1
            print("Bye rectangle...")

        def bigger_or_equal(rect_1, rect_2):
            """returns the biggest rectangle based on the area"""
            if type(rect_1) is not isinstance (rect_1, Rectangle):
                raise TypeError("rect_1 must be an instance of Rectangle")
            if type(rect_2) is not isinstance (rect_2, Rectangle):
                raise TypeError("rect_2 must be an instance of Rectangle")
            if rect_1 == rect_2:
                return rect_1
            elif rect_1 > rect_2:
                return rect_1
            elif rect_2 > rect_1:
                return rect_1

        def square(cls, size=0):
            """returns a rectangle with equal width an height"""
            width == height == size
