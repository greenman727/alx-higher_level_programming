#!/usr/bin/python3
"""Defines a function to divide matrix"""


def matrix_divided(matrix, div):
    """Divides all elements int the matrix"""
    if type(matrix) is not list:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for col in matrix:
        if type(col) is not list:
            raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(col)
        elif size != len(col):
            raise TypeError("Each row of the matrix must have the same size")
        for i in col:
            if type(i) is not int and type(i) is not float:
                raise TypeError(
                        "matrix must be a matrix (list of lists) of \
                                integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in col] for col in matrix]
