#!/usr/bin/python3
"""Defines a function to multiply two matrices by using Numpy"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """A function to multiply two matrices by using Numpy"""
    return (numpy.matmul(m_a, m_b))
