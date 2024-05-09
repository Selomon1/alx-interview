#!/usr/bin/python3
"""Module that calculate the perimeter of the island in grid."""

def island_perimeter(grid):
    """
    Calculate the preimeter of the island described in the grid.

    Args:
        grid (List[List[int]]): Grid represent the island which:
            0 represent - water
            1 represent - land

    Returns:
        int: the perimeter of the island.

    """
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1

                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1

                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1

                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter
