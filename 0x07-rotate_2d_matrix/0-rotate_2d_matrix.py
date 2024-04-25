#!/usr/bin/python3
"""
Rotate 2D Matrix 90 degrees clockwise Module
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a @D matrix degrees clockwise.
    Args:
        matrix (list): The @D matrix to rotate.
    Returns:
        None, The rotation is work in place.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
