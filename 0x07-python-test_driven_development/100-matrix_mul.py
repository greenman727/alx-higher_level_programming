#!/usr/bin/python3
"""A module to multiply two matrices"""


def matrix_mul(m_a, m_b):
    """Divides the two matrices"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    a1 = len(m_a)
    if a1 == 0:
        raise ValueError("m_a can't be empty")
    a2 = None
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if a2 is None:
            a2 = len(i)
            if a2 == 0:
                raise ValueError("m_a can't be empty")
        if a2 != len(i):
            raise TypeError("each row of m_a must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    a3 = None
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if a3 is None:
            a3 = len(i)
            if a3 == 0:
                raise TypeError("m_b can't be empty")
        if a3 != len(i):
            raise TypeError("each row of m_b must be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if a2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new_matrix = []
    for row in range(a1):
        new_row = []
        for col in range(a3):
            n = 0
            for k in range(a2):
                n += m_a[i][k] * m_b[k][j]
            new_row.append(n)
        matrix.append(new_row)

    return new_matrix
