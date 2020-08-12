'''
8x8 board             8       2          2      2     1      1  
different pieces -> "pawn" "bishop" "knight" "rook" "queen" "king"
pawn -> moving -> 1 space forward until you cant.
     -> attacking -> only 1 space diagonal forward
     -> notes cannot go backwards, special is on first move of pawn you can go 2 forward
     
king -> moving -> one space any direction
queen -> moving -> any space any direction
bishop -> moving -> any space only diagonal
rook -> moving -> any space only cardinal (top left bottom right)

you cannot swap friendly pieces


checkmate -> 

'''
class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
    def move(self, multiplier, next_spot_status, cur_row, cur_col, next_row, next_col):
        pass

class King(Piece):
    pass 
        
class Queen(Piece):
    pass 
        
class Castle(Piece):
    pass  
        
class Bishop(Piece):
    pass 
        
class Knight(Piece):
    pass 

class Pawn(Piece):
    def move(self, multiplier, next_spot_status, cur_row, cur_col, next_row, next_col):
        if next_spot_status == 2:
            if (cur_col + 1 == next_col or cur_col - 1 == next_col) and cur_row - multiplier == next_row:
                return True
            else:
                return False
        elif next_spot_status == 1:
            return False
        elif next_spot_status == 0:
            if cur_row - multiplier == next_row and cur_col == next_col:
                return True
            else:
                return False
                
class Game:
    def __init__(self):
        self.board =  [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
        ]
    
    def move(self, cur_row, cur_col, next_row, next_col):
        if not 0<=next_row<=7 or not 0<=next_col<=7:
            return "invalid"
        character = self.board[cur_row][cur_col]
        next_spot = self.board[next_row][next_col]
        next_spot_status = self.check_team(character, next_spot)
        if next_spot_status == 1:
            return "invalid"
        multiplier = 1
        if character.color:
            multiplier = -1
        if character.move(multiplier, next_spot_status, cur_row, cur_col, next_row, next_col):
            self.board[next_row][next_col] = character
            self.board[cur_row][cur_col] = 0
            character.row = next_row
            character.col = next_col
        
            
    def check_team(self, p1,p2):
        if not p2:
            return 0
        if p1.color == p2.color:
            return 1
        else:
            # Check the checkmate conditions
            return 2
            
    
g = Game()
p1 = Pawn(True, 0, 0)
print(p1.color)
g.board[0][0] = p1
print(p1)
print(g.board[0][0])
g.move(0,0,1,0)
print(g.board)
        
        

