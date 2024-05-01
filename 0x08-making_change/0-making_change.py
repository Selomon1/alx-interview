#!/usr/bin/python3
"""Module for making change with the fewest number of coins."""


def makeChange(coins, total):
    """Calculate the fewest number of coins needed to meet a given."""
    if total < 1:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1);
        for coin in coins:
            if amount >= coin:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
