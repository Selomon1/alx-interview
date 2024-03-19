#!/usr/bin/python3
"""
Minimum Operations Module
"""


def minOperations(n):
    """
    Calculates the shortest number of operations required to result in exactly
    n H characters.
    Args:
        n (int): the target number of H characters
    Return:
        int: the minimum number of operations required.
    """
    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
