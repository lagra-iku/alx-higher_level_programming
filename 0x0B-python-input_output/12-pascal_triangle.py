#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n):
    """
    a funct def pascal_triangle(n)

    Returns: a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        line = [1]
        if triangle:
            tmp = triangle[-1]
            for j in range(len(tmp) - 1):
                line.append(tmp[j] + tmp[j + 1])
            line.append(1)
        triangle.append(line)

    return triangle
