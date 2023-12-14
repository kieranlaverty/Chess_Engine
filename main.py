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
    board.set_position("rnbqkbnr/ppp1pppp/8/3p4/4P3/8/PPPP1PPP/RNBQKBNR")
    board.print_board()
    print("")
    board.print_occupied()
    board.legal_moves_readable("d5")



if __name__ == "__main__":
    main()