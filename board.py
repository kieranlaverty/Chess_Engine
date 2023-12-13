
class board():
    def __init__(self):
        self.b = [["0" for _ in range(8)]for i in range(8)]


    def set_board(self):
        self.b[1] = ["wp" for i in range(8)] 
        self.b[0][0] = "wr"
        self.b[0][7] = "wr"
        self.b[0][1] = "wn"
        self.b[0][6] = "wn"
        self.b[0][2] = "wb"
        self.b[0][5] = "wb"
        self.b[0][3] = "wq"
        self.b[0][4] = "wk"

        self.b[6] = ["bp" for i in range(8)]
        self.b[7][0] = "br"
        self.b[7][7] = "br"
        self.b[7][1] = "bn"
        self.b[7][6] = "bn"
        self.b[7][2] = "bb"
        self.b[7][5] = "bb"
        self.b[7][3] = "bq"
        self.b[7][4] = "bk"
        


    def print_board(self):
        for i in self.b:
            rank = ""
            for j in i:
                rank = rank + j + " "
                if j == "0":
                    rank = rank + " "
            print(rank)