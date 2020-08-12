class Piece:
    def __init__(self, top, left, bottom, right):
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right
    
    def rotate_piece(self):
        temp = self.top 
        self.top = self.left
        self.left = self.bottom
        self.bottom = self.right
        self.right = temp
    
    def __str__(self):
        return f"Piece is {self.top} {self.left} {self.bottom} {self.right}"
    
class Puzzle:
    def __init__(self, n , m):
        self.board = [
            [{},None,0],
            [{},0,0],
            [0,0,0]
        ]
    
    def place_piece(self,p1,i,j):
        
        pass

p = Piece(0,0,-2,1)
print(p)
p.rotate_piece()
print(p)

# p = Piece(0,0,-1,2)

def check_edges_between_two_pieces(e1,e2):
    if e1 or e2 == 0:
        return False
    elif e1 + e2 == 0:
        return True
    else:
        return False