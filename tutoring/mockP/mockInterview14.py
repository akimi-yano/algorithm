# Qualities
#   -collaboration
#   -identify scope of the problems (the right scope not too much not too little)
#   -clarity -> explain well. does the other person understand? if they dont, what else can you try?
#                                                               provide additional information or examples
#   -do you understand people? how do you view your own work? do you know your mistakes? what did you learn from them?
#   -even if you dont know something, can you make an educated guess as to why or what might be missing from what you know
#   -curiosity -> willingness to learn more -> towards the end
  
# Approaches
#   -keep it as simple as possible
#   -pros vs cons -> can you explain?
#   -how you explain (politely) if you dont understand -- then politely ask for clarification
#   -solving the problem carefully constantly think about what they mentioned over and over.
#     is it absolutely needed?
#   -think ahead and think consistently and be flexible to change
#   -think about abstracting / efficiency (last priority)
#   # SD:
#   # Did you consider scalability and robustness when designing systems?
#   # Horizontal vs Vertical, volume of traffic , CAP Theorem, possible pitfalls
  
# are you relevant? -> have you done stuff related recently? talk about similar cases if you're stuck

'''
Algorithms to review: -> should be able to write in 5-10 mins  
# validate bst
# bst problems (dfs, bfs)
# rabbit problem
# matrix (dfs bfs)
# heaps, priority queue
# binary search
# all possible permutations / combinations of a word
# ascii -> ord(letter)
# SLL -> removing duplicates / reversing a list / adding 1 to the digits
# sliding window
# product / sum of subarray
# k top ___ of ____
# restructuring json data or objects into different array of objects based on different sort criteria
# sort by frequency and parity
# adding two binary strings
# binary to decimal

# -> read the theory and make simple algo.
# decimal to hex
# hex to decimal
# binary to hex
# hex to binary

# using % and // to chop digits and process them one by one
# reversing integers without conversion to strings

# google this:
# how to raise errors in python

# practice using else with for loop


and review oop that I did and system design I did and light reading 
simpler version of google doc for mobile

review everything I have done !!!!!!

Don't memorize but practice one by one !

start from small pieces ! 

start with pseurdo code and if I dont have time to finish coding - I have the code !
'''
'''
Making 2048.
"swipe" up left down right
numbers that are the same double.
if 2048 is made, then game is over user wins.
no valid moves = lost.
2 number - > (2) and (2 or 4)
board :  4*4
[[0,0,4,0],
 [0,0,2,0],
 [0,0,2,0],
 [0,0,0,0]]
hjkl - left, down, top, right
if invalid -> dont change 
'''
# small -> large
# make smallest piece first - because large depends on small 
import random
class Tile:
    def __init__(self, number):
        self.number = number
        self.is_merged = False
    
    def __str__(self):
        return f"{self.number}"

    
class Board:
    def __init__(self):
        self.storage = [
            [2,4,8,16],
            [4,4,4,None],
            [2,None,None,None],
            [2,4,8,16]
            ]
        self.storage[2][2] = Tile(2)
        self.storage[1][1] = Tile(random.randint(0,1) * 2 + 2)
        self.has_moved = False
        self.count = 2

    def move(self, direction):
        if direction == "up":
            for i in range(1):
                for j in range(4):
                    current_i = i
                    while True:
                        # hit a wall
                        if current_i == 0:
                            break
                        # hit a different number not None
                        if self.storage[current_i][j].number != self.storage[current_i - 1][j].number and self.storage[current_i - 1][j] not None:
                            break
                        # hit a number with is_merged == True
                        if self.storage[current_i - 1][j].is_merged:
                            break
                        # same number and is_merged == False
                        if not self.storage[current_i - 1][j].is_merged and self.storage[current_i][j].number == self.storage[current_i - 1][j].number
                            self.storage[current_i - 1][j].number *= 2
                            self.storage[current_i - 1][j].is_merged = True
                        if self.storage[current_i-1][j] == None:
                            self.storage[current_i - 1][j] = self.storage[current_i][j]
                            self.storage[current_i][j] = None
                        current_i -= 1
            # reset is_merged
            for i in range(4):
                for j in range(4):
                    self.storage[i][j].is_merged = False
        if direction == "down":
                    i + 1

        if direction == "left":
                    j - 1

        if direction == "right":
                    j + 1
        # depending on direction
        # we shift pieces based on matching or empty space
        
        for
        # we can check here for 2048 when combining
            if something moves:
                self.has_moved = True
        
        
        self.check_win()
        pass

    def add_piece(self):
        if self.has_moved:
            if self.scan_valid():
                self.storage[i][j] = Tile(random.randint(0,1) * 2 + 2)
        self.has_moved = False
    
    def scan_valid(self):
        if self.count < 16:
            return True
        return False
        
    def check_win(self):
        for 
            for
                if there is 2048:
                    return "Win"
                if up down left right = current:
                    return "OK"
        if not self.scan_valid():
            return "Lost"
    

# https://play2048.co/




