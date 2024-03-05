#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's Triangle based on the specified number of rows
    Args:
        n: An integer specified the number of rows in the Pascal's Triangle
    Returns: A list of lists of integers specified
    """
    if n <= 0:
        return {}

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1] + [prev_row[j - 1] + prev_row[j] for j in range(1, i)]
        new_row += [1]
        triangle.append(new_row)

    return triangle
