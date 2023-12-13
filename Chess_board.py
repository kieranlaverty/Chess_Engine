import numpy as np
import chess

class board():

    def __init__(self):
        self.board = chess.Board()

    def print_legal_moves(self):
        print(self.board.legal_moves)
