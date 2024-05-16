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
    def generate_primes_up_to(n):
        """Generate a list of prime numbers up to 'max_number' using sieve."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def game(n):
        primes = [i for i in range(2, n + 1) if generate_primes_up_to(i)]
        player = 0
        while primes:

            for prime in primes:
                primes = [p for p in primes if p % prime != 0]
                player = 1 - player
                break
        return player

    score = [0, 0]
    for n in nums:
        score[game(n)] += 1

    if score[0] > score[1]:
        return "Maria"
    elif score[0] < score[1]:
        return "Ben"
    else:
        return None
