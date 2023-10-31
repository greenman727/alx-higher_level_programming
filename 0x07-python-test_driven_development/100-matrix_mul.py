#!/usr/bin/python3
"""Defines a function to multiply 2 matrices"""


def matrix_mul(m_a, m_b):
    """A function to multiply two matrices"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    col1 = len(m_a)
    if col1 == 0:
        raise ValueError("m_a can't be empty")
    col2 = None
    for i in (m_a):
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if col2 is None:
            col2 = len(i)
            if col2 == 0:
                raise ValuError("m_a can't be empty")
        if col2 != len(i):
            raise TypeError("each row of m_a must be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if type(m_b) == 0:
        raise ValueError("m_b can't be empty")
    col3 = None
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if col3 is None:
            col3 = len(i)
            if col3 == 0:
                raise ValueError("m_b can't be empty")
            if col3 != len(i):
                raise TypeError("each row of m_b must be of the same size")
            for j in i:
                if type(j) is not int and type(j) is not float:
                    raise TypeError(
                            "m_b should contain only integers or floats")
    if col2 != len(m_b):
        raise TypeError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(col1):
        col = []
        for j in range(col3):
            a = 0
            for k in range(col2):
                a += m_a[i][k] * m_b[k][j]
                col.append(a)
            matrix.append(col)
    return matrix

