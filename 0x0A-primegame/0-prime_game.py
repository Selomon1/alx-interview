#!/usr/bin/python3
"""Module for determining the winner of multiple  of prime removal game."""


def isWinner(x, nums):
    """
    Determine the winner of rounds of a prime removal game.

    Args:
        x (int): Number of rounds game played.
        nums (list[int]): List of integers representing

    Returns:
        str or None: Name of the player

    """
    def sieve_of_eratosthenes(max_num):
        """Generate a list of prime numbers up to 'max_number' using sieve."""
        is_prime = [True] * (max_num + 1)
        p = 2
        while (p * p <= max_num):
            if is_prime[p]:
                for i in range(p * p, max_num + 1, p):
                    is_prime[i] = False

            p += 1
        is_prime[0], is_prime[1] = False, False
        primes = [p for p in range(max_num + 1) if is_prime[p]]
        return primes

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        available_primes = [p for p in primes if p <= n]
        remaining_numbers = set(range(1, n + 1))

        turn = 0
        while True:
            if not available_primes:
                break

            chosen_prime = available_primes.pop(0)
            multiples = set(range(chosen_prime, n + 1, chosen_prime))

            remaining_numbers.difference_update(multiples)

            turn = 1 - turn

        if turn == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
