#!/usr/bin/python3
"""
Module: 12-pascal_triangle

This module provides a function that returns Pascal’s triangle
as a list of lists of integers.

Author: ALU Higher Level Programming
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows.

    Args:
        n (int): Number of rows to generate.

    Returns:
        list of lists: A list containing n lists,
        each representing a row in Pascal’s triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # First element is always 1
        prev_row = triangle[-1]

        # Middle values: sum of two values above
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
