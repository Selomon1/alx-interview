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
            return []
        sieve = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if sieve[p] == True:
                for i in range(p * p, n + 1, p):
                    sieve[i] = False

            p += 1
        return [p for p in range(2, n + 1) if sieve[p]]

    def can_win(n):
        primes = generate_primes_up_to(n)
        if not primes:
            return False

        turn = 0
        remaining_numbers = set(range(1, n + 1))

        while True:
            possible_moves = [p for p in primes if p in remaining_numbers]
            if not possible_moves:
                return turn

            for move in possible_moves:
                for num in range(move, n + 1, move):
                    if num in remaining_numbers:
                        remaining_numbers.remove(num)

            turn = 1 - turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = can_win(n)
        if winner == 0:
            maria_wins += 1
        elif winner == 1:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
