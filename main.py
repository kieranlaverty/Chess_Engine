"""
this is to be a chess engine

__________
for the chess libary I am using 
https://python-chess.readthedocs.io/en/latest/

This is to make moving pieces or writing pgn files easy
"""

import board as b


def main():
    board = b.board()
    board.set_board()
    for m in board.legal_moves("e2"):
        print(board.get_square_notation(m))



if __name__ == "__main__":
    main()