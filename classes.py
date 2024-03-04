class piece():
    all_pieces = []
    def __init__(self,color:int,position:list):   # 0 = White , 1 = Dark
        self.color = color
        self.position = position
        #piece.all_pieces.append(self)

    def __repr__(self):
        return f"{self.color} [{self.position}]"
    
class pawns(piece):
    def __init__(self, color: int, position: list):
        super().__init__(color, position)
        self.type = 0
        piece.all_pieces.append(self)
        
class knight(piece):
    def __init__(self, color: int, position: list):
        super().__init__(color, position)
        self.type = 1
        piece.all_pieces.append(self)

class bishop(piece):
    def __init__(self, color: int, position: list):
        super().__init__(color, position)
        self.type = 2
        piece.all_pieces.append(self)

class rook(piece):
    def __init__(self, color: int, position: list):
        super().__init__(color, position)
        self.type = 3
        piece.all_pieces.append(self)

class queen(piece):
    def __init__(self, color: int, position: list):
        super().__init__(color, position)
        self.type = 4
        piece.all_pieces.append(self)

class king(piece):
    def __init__(self, color: int, position: list):
        super().__init__(color, position)
        self.type = 5
        piece.all_pieces.append(self)






