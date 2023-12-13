
class Pawn():
    #constuctor
    def __init__(self, color) -> None:
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
    
    def color(self):
        return self.color
    

class Rook():
    def __init__(self, color) -> None:
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
    
    def color(self):
        return self.color
    
class Knight():
    def __init__(self, color) -> None:
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
    
    def color(self):
        return self.color
    
class Bishop():
    def __init__(self, color) -> None:
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

    def color(self):
        return self.color
    
class Queen():
    def __init__(self, color) -> None:
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

    def color(self):
        return self.color
    
class King():
    def __init__(self, color) -> None:
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
    
    def color(self):
        return self.color
    