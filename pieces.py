
class Pawn():
    #constuctor
    def __init__(self, color):
        try:
            if (color == "w"):
                self.color = "w"
            elif (color == "b"):
                self.color = "b"
            else:
                raise
        except:
            print("Please enter a valid color choose of 'w' or 'b' ")


    def __str__ (self) -> str:
        return self.color + "p"
    
class Rook():
    def __init__(self, color):
        try:
            if (color == "w"):
                self.color = "w"
            elif (color == "b"):
                self.color = "b"
            else:
                raise
        except:
            print("Please enter a valid color choose of 'w' or 'b' ")

    def __str__ (self) -> str:
        return self.color + "r"

class Knight():
    def __init__(self, color):
        try:
            if (color == "w"):
                self.color = "w"
            elif (color == "b"):
                self.color = "b"
            else:
                raise
        except:
            print("Please enter a valid color choose of 'w' or 'b' ")

    def __str__ (self) -> str:
        return self.color + "n"
    
class Bishop():
    def __init__(self, color):
        try:
            if (color == "w"):
                self.color = "w"
            elif (color == "b"):
                self.color = "b"
            else:
                raise
        except:
            print("Please enter a valid color choose of 'w' or 'b' ")

    def __str__ (self) -> str:
        return self.color + "b"

class Queen():
    def __init__(self, color):
        try:
            if (color == "w"):
                self.color = "w"
            elif (color == "b"):
                self.color = "b"
            else:
                raise
        except:
            print("Please enter a valid color choose of 'w' or 'b' ")

    def __str__ (self) -> str:
        return self.color + "q"

class King():
    def __init__(self, color):
        try:
            if (color == "w"):
                self.color = "w"
            elif (color == "b"):
                self.color = "b"
            else:
                raise
        except:
            print("Please enter a valid color choose of 'w' or 'b' ")

    def __str__ (self) -> str:
        return self.color + "k"