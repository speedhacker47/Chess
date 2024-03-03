class piece():
    all_pieces = []
    def __init__(self,color:int,position:list):   # 0 = White , 1 = Dark
        self.color = color
        self.position = position
        piece.all_pieces.append(self)

    def __repr__(self):
        return f"{self.color} [{self.position}]"
    
class pawns(piece):
    def __init__(self, color: int, position: list):
        super().__init__(color, position)
        self.type = 0
        
class knight(piece):
    def __init__(self, color: int, position: list):
        super().__init__(color, position)
        self.type = 1

class bishop(piece):
    def __init__(self, color: int, position: list):
        super().__init__(color, position)
        self.type = 2

class rook(piece):
    def __init__(self, color: int, position: list):
        super().__init__(color, position)
        self.type = 3

class queen(piece):
    def __init__(self, color: int, position: list):
        super().__init__(color, position)
        self.type = 4

class king(piece):
    def __init__(self, color: int, position: list):
        super().__init__(color, position)
        self.type = 5






