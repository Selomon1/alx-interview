#!/usr/bin/python3

import sys


def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, row, N, solutions):
    if row == N:
        queens_positions = []
        for r in range(N):
            for c in range(N):
                if board[r][c] == 1:
                    queens_positions.append([r, c])
        solutions.append(queens_positions)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve(board, row + 1, N, solutions)
            board[row][col] = 0


def nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve(board, 0, N, solutions)

    for solution in solutions:
        print([[r, c] for r, c in solution])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
