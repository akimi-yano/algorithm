# 1861. Rotating the Box
# Medium

# 128

# 14

# Add to List

# Share
# You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

# A stone '#'
# A stationary obstacle '*'
# Empty '.'
# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

# It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

# Return an n x m matrix representing the box after the rotation described above.

 

# Example 1:



# Input: box = [["#",".","#"]]
# Output: [["."],
#          ["#"],
#          ["#"]]
# Example 2:



# Input: box = [["#",".","*","."],
#               ["#","#","*","."]]
# Output: [["#","."],
#          ["#","#"],
#          ["*","*"],
#          [".","."]]
# Example 3:



# Input: box = [["#","#","*",".","*","."],
#               ["#","#","#","*",".","."],
#               ["#","#","#",".","#","."]]
# Output: [[".","#","#"],
#          [".","#","#"],
#          ["#","#","*"],
#          ["#","*","."],
#          ["#",".","*"],
#          ["#",".","."]]
 

# Constraints:

# m == box.length
# n == box[i].length
# 1 <= m, n <= 500
# box[i][j] is either '#', '*', or '.'.


# This solution works:

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROW = len(box)
        COL = len(box[0])
        newbox = []
        for col in range(COL):
            temp = []
            for row in range(ROW):
                temp.append(box[row][col])
            temp.reverse()
            newbox.append(temp)
        
        def helper(rowlim, col):
            if rowlim == -1:
                return
            count = 0
            start = 0
            for row in range(rowlim+1):
                if newbox[row][col] == "*":
                    start = row+1
                    count = 0
                if newbox[row][col] == "#":
                    count += 1
            # print(count)
            if count == 0:
                return
            idx = rowlim - count +1
            for row in range(start, idx):
                newbox[row][col] = "."
            for row in range(idx, rowlim+1):
                newbox[row][col] = "#"
        # print(newbox)
        ROW = len(newbox)
        COL = len(newbox[0])
        for col in range(COL):
            for row in range(ROW):
                if newbox[row][col] == "*" or (row == ROW -1 and newbox[row][col] == "#"):
                    helper(row-1, col)
                    
                elif row == ROW -1 and newbox[row][col] == ".":
                    helper(row, col)
                    
#         for row in range(ROW):
#             for col in range(COL//2):
#                 newbox[row][col], newbox[row][COL-1-col] = newbox[row][COL-1-col], newbox[row][col]
        return newbox


# This solution works - optimization:


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROW = len(box)
        COL = len(box[0])
        newbox = []
        for col in range(COL):
            temp = []
            for row in range(ROW):
                temp.append(box[row][col])
            temp.reverse()
            newbox.append(temp)
        
        for col in range(len(newbox[0])):
            blocked_index = len(newbox)
            for row in range(len(newbox)-1, -1, -1):
                if newbox[row][col] == '#':
                    newbox[row][col] = '.'
                    newbox[blocked_index-1][col] = '#'
                    blocked_index -= 1
                if newbox[row][col] == '*':
                    blocked_index = row
                if newbox[row][col] == '.':
                    pass
        return newbox
                    
        