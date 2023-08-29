#!/usr/bin/python3

"""defines a class square"""

class square:

    """Representes a square attributes"""

    def __init__(self, size=0):
        """initializes a square
        Args:
        size (int): size of a side of a square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

