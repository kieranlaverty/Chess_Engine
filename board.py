import pieces as p

class board():

    #this is the constructor
    #create a var b to hold the chess board
    def __init__(self):
        self.b = [["0" for _ in range(8)]for i in range(8)]

    #This function set the board in the initial starting position
    """
    [
    [a8, b8, c8, d8, e8, f8, g8, h8],
    [a7, b7, c7, d7, e7, f7, g7, h7],
    [a6, b6, c6, d6, e6, f6, g6, h6],
    [a5, b5, c5, d5, e5, f5, g5, h5],
    [a4, b4, c4, d4, e4, f4, g4, h4],
    [a3, b3, c3, d3, e3, f3, g3, h3],
    [a2, b2, c2, d2, e2, f2, g2, h2],
    [a1, b1, c1, d1, e1, f1, g1, h1],
    """
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

    #This function sets a board to a custom position given a string
    def set_position(self, position):
        square_list = []
        holder = []
        for s in position:
            if s == "/":
                pass
            elif s.isnumeric():
                for _ in range(int(s)):
                    holder.append("0")
            else:
                holder.append(s)
            
            if len(holder) == 8:
                square_list.append(holder)
                holder = []  

        for i in range(8):
            for j in range(8):
                if square_list[i][j] == 0:
                    pass
                elif square_list[i][j].isupper():
                    if square_list[i][j] == "R":
                        self.b[i][j] = p.Rook("w")
                    elif square_list[i][j] == "N":
                        self.b[i][j] = p.Knight("w")
                    elif square_list[i][j] == "B":
                        self.b[i][j] = p.Bishop("w")
                    elif square_list[i][j] == "Q":
                        self.b[i][j] = p.Queen("w")
                    elif square_list[i][j] == "K":
                        self.b[i][j] = p.King("w")
                    elif square_list[i][j] == "P":
                        self.b[i][j] = p.Pawn("w")
                elif square_list[i][j].isupper() == False:
                    if square_list[i][j] == "r":
                        self.b[i][j] = p.Rook("b")
                    elif square_list[i][j] == "n":
                        self.b[i][j] = p.Knight("b")
                    elif square_list[i][j] == "b":
                        self.b[i][j] = p.Bishop("b")
                    elif square_list[i][j] == "q":
                        self.b[i][j] = p.Queen("b")
                    elif square_list[i][j] == "k":
                        self.b[i][j] = p.King("b")
                    elif square_list[i][j] == "p":
                        self.b[i][j] = p.Pawn("b")   

    #retuns an list with 1 being occupied by white, 2 if by black, and 0 being unoccupied
    #white == 1, Black == 2, 0 == no piece
    def occupied_sq(self):
        occupied = [["0" for _ in range(8)]for i in range(8)]
        for rank in range(8):
            for file in range(8):
                if self.b[rank][file] != "0":
                    if self.b[rank][file].color == "w":
                        occupied[rank][file] = "1"
                    else:
                        occupied[rank][file] = "2"
        
        return occupied

    #given a square a list is returned of all the posible square the piece could move
    def legal_moves(self, square):
        occupied = self.occupied_sq()
        if (self.b[square[0]][square[1]] == "0"):
            return "Unoccupied Square"
        else:
            possible = self.b[square[0]][square[1]].legal_moves(square, occupied)
            return possible

    #given algebric notation of a square the board list location is returned
    #return (rank, file)
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
        

        rank = abs(int(square[1]) - 8)

        return (rank, file)
    
    #given the board list location algebric notation is returned for the square
    def get_square_notation(self, square):
        if square[1] == 0:
            file = "a"
        elif square[1] == 1:
            file = "b"
        elif square[1] == 2:
            file = "c"
        elif square[1] == 3:
            file = "d"
        elif square[1] == 4:
            file = "e"
        elif square[1] == 5:
            file = "f"
        elif square[1] == 6:
            file = "g"
        elif square[1] == 7:
            file = "h"

        rank =   square[0]  + 1

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
    
    #This function prints out the occupied sq on the board in a readable format
    def print_occupied(self):
        for i in self.occupied_sq():
            rank = ""
            for j in i:
                try:
                    rank = rank + j + " "
                except:
                    rank = rank + str(j) + " "

            print(rank)

    #This function prints out the playable moves in a readable format
    def legal_moves_readable(self, square):
        placement = self.get_square(square)
        moves = self.legal_moves(placement)
        if len(moves) > 0:
            for m in moves:
                print(self.get_square_notation(m))
        else:
            print("no possible moves")