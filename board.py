import pieces as p

class board():
    def __init__(self):
        self.b = [["0" for _ in range(8)]for i in range(8)]

    #This function set the board in the initial starting position
    def set_board(self):
        self.b[6] = [ p.Pawn("w") for j in range(8)] 
        self.b[7][0] = p.Rook("w")
        self.b[7][7] = p.Rook("w")
        self.b[7][1] = p.Knight("w")
        self.b[7][6] = p.Knight("w")
        self.b[7][2] = p.Bishop("w")
        self.b[7][5] = p.Bishop("w")
        self.b[7][3] = p.Queen("w")
        self.b[7][4] = p.King("w")

        self.b[1] = [ p.Pawn("b") for i in range(8)]
        self.b[0][0] = p.Rook("b")
        self.b[0][7] = p.Rook("b")
        self.b[0][1] = p.Knight("b")
        self.b[0][6] = p.Knight("b")
        self.b[0][2] = p.Bishop("b")
        self.b[0][5] = p.Bishop("b")
        self.b[0][3] = p.Queen("b")
        self.b[0][4] = p.King("b")

    #retuns an list with 1 being occupied by white, 2 if by black, and 0 being unoccupied
    def occupied_sq(self):
        occupied = [["0" for _ in range(8)]for i in range(8)]
        for i in range(8):
            for j in range(8):
                if self.b[i][j] != "0":
                    if self.b[i][j].color == "w":
                        occupied[i][j] = "1"
                    else:
                        occupied[i][j] = "2"
        
        return occupied

    def legal_moves(self, square):
        placement = self.get_square(square)
        occupied = self.occupied_sq()
        possible = self.b[placement[0]][placement[1]].legal_moves(placement, occupied)
        return possible

    
    def get_square(self, square):
        if square[0] == "a":
            file = 0
        elif square[0] == "b":
            file = 1
        elif square[0] == "c":
            file = 2 
        elif square[0] == "d":
            file = 3
        elif square[0] == "e":
            file = 4
        elif square[0] == "f":
            file = 5
        elif square[0] == "g":
            file = 6
        elif square[0] == "h":
            file = 7
        

        rank = int(square[1]) - 1

        return (rank, file)
    
    def get_square_notation(self, square):
        if square[0] == 0:
            file = "a"
        elif square[0] == 1:
            file = "b"
        elif square[0] == 2:
            file = "c"
        elif square[0] == 3:
            file = "d"
        elif square[0] == 4:
            file = "e"
        elif square[0] == 5:
            file = "f"
        elif square[0] == 6:
            file = "g"
        elif square[0] == 7:
            file = "h"
        

        rank = int(square[1]) + 1

        return file + str(rank)

    #This function prints out the board in a readable format
    def print_board(self):
        for i in self.b:
            rank = ""
            for j in i:
                try:
                    rank = rank + j + " "
                    if j == "0":
                        rank = rank + " "
                except:
                    rank = rank + str(j) + " "

            print(rank)