# 1728. Cat and Mouse II
# Hard

# 4

# 8

# Add to List

# Share
# A game is played by a cat and a mouse named Cat and Mouse.

# The environment is represented by a grid of size rows x cols, where each element is a wall, floor, player (Cat, Mouse), or food.

# Players are represented by the characters 'C'(Cat),'M'(Mouse).
# Floors are represented by the character '.' and can be walked on.
# Walls are represented by the character '#' and cannot be walked on.
# Food is represented by the character 'F' and can be walked on.
# There is only one of each character 'C', 'M', and 'F' in grid.
# Mouse and Cat play according to the following rules:

# Mouse moves first, then they take turns to move.
# During each turn, Cat and Mouse can jump in one of the four directions (left, right, up, down). They cannot jump over the wall nor outside of the grid.
# catJump, mouseJump are the maximum lengths Cat and Mouse can jump at a time, respectively. Cat and Mouse can jump less than the maximum length.
# Staying in the same position is allowed.
# Mouse can jump over Cat.
# The game can end in 4 ways:

# If Cat occupies the same position as Mouse, Cat wins.
# If Cat reaches the food first, Cat wins.
# If Mouse reaches the food first, Mouse wins.
# If Mouse cannot get to the food within 1000 turns, Cat wins.
# Given a rows x cols matrix grid and two integers catJump and mouseJump, return true if Mouse can win the game if both Cat and Mouse play optimally, otherwise return false.

 

# Example 1:



# Input: grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
# Output: true
# Explanation: Cat cannot catch Mouse on its turn nor can it get the food before Mouse.
# Example 2:



# Input: grid = ["M.C...F"], catJump = 1, mouseJump = 4
# Output: true
# Example 3:

# Input: grid = ["M.C...F"], catJump = 1, mouseJump = 3
# Output: false
# Example 4:

# Input: grid = ["C...#","...#F","....#","M...."], catJump = 2, mouseJump = 5
# Output: false
# Example 5:

# Input: grid = [".M...","..#..","#..#.","C#.#.","...#F"], catJump = 3, mouseJump = 1
# Output: true
 

# Constraints:

# rows == grid.length
# cols = grid[i].length
# 1 <= rows, cols <= 8
# grid[i][j] consist only of characters 'C', 'M', 'F', '.', and '#'.
# There is only one of each character 'C', 'M', and 'F' in grid.
# 1 <= catJump, mouseJump <= 8


# This approach does not work
# class Solution:
#     def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
#         self.M = len(grid)
#         self.N = len(grid[0])
#         self.CJ = catJump
#         self.MJ = mouseJump
#         mrow, mcol, crow, ccol = 0, 0, 0, 0
        
#         for row in range(self.M):
#             for col in range(self.N):
#                 if grid[row][col] == 'M':
#                     mrow, mcol = row, col
#                 if grid[row][col] == 'C':
#                     crow, ccol = row, col
                    
#         @lru_cache(None)
#         def helper(mrow, mcol, crow, ccol, turn):
#             if not (0 <= mrow <= self.M-1) or not (0 <= crow <= self.M-1) or not (0 <= mcol <= self.N-1) or not (0 <= ccol <= self.N-1) or (grid[mrow][mcol] == '#') or (grid[crow][ccol] == '#'):
#                 return False
#             if turn > 1000:
#                 return False
#             if grid[crow][ccol] == grid[mrow][mcol]:
#                 return False
#             if grid[crow][ccol] == 'F':
#                 return False
#             if grid[mrow][mcol] == 'F':
#                 print(mrow, mcol, turn, crow, ccol)
#                 return True
            
#             ans = False
#             if turn % 2 != 0:
#                 for step in range(self.MJ, -1, -1):
#                     ans |= helper(mrow, mcol+step, crow, ccol, turn+1)
#                     ans |= helper(mrow, mcol-step, crow, ccol, turn+1)
#                     ans |= helper(mrow+step, mcol, crow, ccol, turn+1)
#                     ans |= helper(mrow-step, mcol, crow, ccol, turn+1)
#             else:
#                 for step in range(self.CJ, -1, -1):
#                     ans |= helper(mrow, mcol, crow, ccol+step, turn+1)
#                     ans |= helper(mrow, mcol, crow, ccol-step, turn+1)
#                     ans |= helper(mrow, mcol, crow+step, ccol, turn+1)
#                     ans |= helper(mrow, mcol, crow-step, ccol, turn+1)
#             return ans
#         return helper(mrow, mcol, crow, ccol, 1)



# YES THIS SOLUTION WORKS !!!!!

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        self.M = len(grid)
        self.N = len(grid[0])
        self.CJ = catJump
        self.MJ = mouseJump
        mrow, mcol, crow, ccol = 0, 0, 0, 0
        self.available = 0
        for row in range(self.M):
            for col in range(self.N):
                if grid[row][col] != '#':
                    self.available += 1
                if grid[row][col] == 'M':
                    mrow, mcol = row, col
                if grid[row][col] == 'C':
                    crow, ccol = row, col
                    
        @lru_cache(None)
        def helper(mrow, mcol, crow, ccol, turn):
            if not (0 <= mrow <= self.M-1) or not (0 <= crow <= self.M-1) or not (0 <= mcol <= self.N-1) or not (0 <= ccol <= self.N-1) or (grid[mrow][mcol] == '#') or (grid[crow][ccol] == '#'):
                return False
            # all the possible spots (non-#spots) * 2 (cat and mouse) which is all the [possibilities]
            if turn > self.available * 2:
                return False
            if (crow == mrow) and (ccol == mcol):
                return False
            if grid[crow][ccol] == 'F':
                return False
            if grid[mrow][mcol] == 'F':
                return True
            
            if turn % 2 != 0:
                for row, col in ((1,0),(-1,0),(0,1),(0,-1)):
                    for step in range(self.MJ+1):
                        newrow, newcol = row * step, col * step
                        if (0 <= mrow+newrow <= self.M-1) and (0 <= mcol+newcol <= self.N-1) and grid[mrow+newrow][mcol+newcol] != '#':
                            if helper(mrow+newrow, mcol+newcol, crow, ccol, turn+1):
                                return True
                        else:
                            break
                return False
            else:
                for row, col in ((1,0),(-1,0),(0,1),(0,-1)):
                    for step in range(self.CJ+1):
                        newrow, newcol = row * step, col * step
                        if (0 <= crow+newrow<= self.M-1) and (0 <= ccol+newcol <= self.N-1) and grid[crow+newrow][ccol+newcol] != '#':
                            if not helper(mrow, mcol, crow+newrow, ccol+newcol, turn+1):
                                return False
                        else:
                            break
                            
                return True
        return helper(mrow, mcol, crow, ccol, 1)