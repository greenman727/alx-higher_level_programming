#!/usr/bin/python3
"""Defines a function that returns list representing the Pascal's triangle"""


def pascal_triangle(n):
    """Represent a Pascal Triangle of size n"""
    if n <= 0:
        return []
    
    triangles = [[1]]
    while len(triangles) != n:
        tria = triangles[-1]
        tmp = [1]
        for i in range(len(tria) - 1):
            tmp.append(tria[i] + tria[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
