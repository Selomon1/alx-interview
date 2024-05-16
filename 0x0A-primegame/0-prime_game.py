#!/usr/bin/python3
"""Module for determining the winner of multiple  of prime removal game."""


def sieve_eratosthenes(max_n):
    """List of prime numbers."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    for start in range(2, int(max_n ** 0.5) + 1):
        if is_prime[start]:
            for i in range(start * start, max_n + 1, start):
                is_prime[i] = False

    return is_prime


def count_primes_up_to(max_n, is_prime):
    """Return list of the count of primes."""
    prime_count = [0] * (max_n + 1)
    count = 0
    for i in range(1, max_n + 1):
        if is_prime[i]:
            count += 1
        prime_count[i] = count
    return prime_count


def isWinner(x, nums):
    """
    Determine the winner of rounds of a prime removal game.

    Args:
        x (int): Number of rounds game played.
        nums (list[int]): List of integers representing

    Returns:
        str or None: Name of the player

    """
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    is_prime = sieve_eratosthenes(max_n)
    prime_count = count_primes_up_to(max_n, is_prime)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
