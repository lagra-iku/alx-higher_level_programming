#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
This is a program that solves the N queens problem.
"""


def check(piece, col):
    """
    check queen in column
    Args:
        col (int): column being checked
        piece (int): piece to check
    Returns:
        boolean of status if a queen
    """
    for i in range(col):
        if piece[i] == piece[col]:
            return False
        if abs(piece[i] - piece[col]) == abs(i - col):
            return False
    return True


def change(piece, col):
    """
    change queen when no issues
    Args:
        col (int): column being checked
        piece (int): piece to check
    Returns:
        boolean of status if a queen
    """
    length = len(piece)
    j = 0

    if col == length:
        result = []

        for i in range(len(piece)):
            result.append([i, piece[i]])

        print(result)
        return True

    piece[col] = -1

    while(piece[col] < length - 1 or j == 1):
        piece[col] = piece[col] + 1
        if check(piece, col) is True:
            if col != length:
                change(piece, (col + 1))
            else:
                j = 1
                break
    return True


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    piece = []
    length = int(sys.argv[1])
    for i in range(length):
        piece.append(-1)

    change(piece, 0)
