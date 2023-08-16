#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for col in matrix:
        answer = list(map(lambda a: a**2, col))
        new_matrix.append(answer)
    return new_matrix
