#!/usr/bin/python3
"""Module for making change with the fewest number of coins."""


def makeChange(coins, total):
    """Calculate the fewest number of coins needed to meet a given."""
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    num_coins_used = 0
    remaining_total = total
    current_coin_index = 0

    while remaining_total > 0:
        if current_coin_index >= len(coins):
            return -1

        if remaining_total >= coins[current_coin_index]:
            remaining_total -= coins[current_coin_index]
            num_coins_used += 1
        else:
            current_coin_index += 1

    return num_coins_used
