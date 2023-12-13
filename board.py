import pieces as p

class board():
    def __init__(self):
        self.b = [["0" for _ in range(8)]for i in range(8)]

    #This function set the board in the initial starting position
    def set_board(self):
        self.b[1] = [ p.Pawn("w") for j in range(8)] 
        self.b[0][0] = p.Rook("w")
        self.b[0][7] = p.Rook("w")
        self.b[0][1] = p.Knight("w")
        self.b[0][6] = p.Knight("w")
        self.b[0][2] = p.Bishop("w")
        self.b[0][5] = p.Bishop("w")
        self.b[0][3] = p.Queen("w")
        self.b[0][4] = p.King("w")

        self.b[6] = [ p.Pawn("b") for i in range(8)]
        self.b[7][0] = p.Rook("b")
        self.b[7][7] = p.Rook("b")
        self.b[7][1] = p.Knight("b")
        self.b[7][6] = p.Knight("b")
        self.b[7][2] = p.Bishop("b")
        self.b[7][5] = p.Bishop("b")
        self.b[7][3] = p.Queen("b")
        self.b[7][4] = p.King("b")

    #retuns an list with 1 being occupied and 0 being unoccupied
    def occupied_sq(self):
        occupied = [["0" for _ in range(8)]for i in range(8)]
        for i in range(8):
            for j in range(8):
                if self.b[i][j] != "0":
                    occupied[i][j] = "1"
        
        return occupied


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