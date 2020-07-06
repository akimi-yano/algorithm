# 1504. Count Submatrices With All Ones

# User Accepted:1673
# User Tried:2441
# Total Accepted:1753
# Total Submissions:3713
# Difficulty:Medium
# Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.

# Example 1:

# Input: mat = [[1,0,1],
#               [1,1,0],
#               [1,1,0]]
# Output: 13
# Explanation:
# There are 6 rectangles of side 1x1.
# There are 2 rectangles of side 1x2.
# There are 3 rectangles of side 2x1.
# There is 1 rectangle of side 2x2. 
# There is 1 rectangle of side 3x1.
# Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
# Example 2:

# Input: mat = [[0,1,1,0],
#               [0,1,1,1],
#               [1,1,1,0]]
# Output: 24
# Explanation:
# There are 8 rectangles of side 1x1.
# There are 5 rectangles of side 1x2.
# There are 2 rectangles of side 1x3. 
# There are 4 rectangles of side 2x1.
# There are 2 rectangles of side 2x2. 
# There are 2 rectangles of side 3x1. 
# There is 1 rectangle of side 3x2. 
# Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
# Example 3:

# Input: mat = [[1,1,1,1,1,1]]
# Output: 21
# Example 4:

# Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
# Output: 5

# Constraints:

# 1 <= rows <= 150
# 1 <= columns <= 150
# 0 <= mat[i][j] <= 1


# this does not work --- look below
# class Solution:
#     def numSubmat(self, mat: List[List[int]]) -> int:
#         self.counter = 0 
#         self.max_row = len(mat)
#         self.max_col = len(mat[0])
        
#         def check(t_row,t_col,a_row,a_col):
#             if a_row>t_row or a_col>t_col:
#                 return 
#             if mat[a_row][a_col]==0:
#                 return 
#             if t_row == a_row and t_col == a_col and mat[a_row][a_col]==1:
#                 self.counter+=1
#                 return 
#             check(t_row,t_col,a_row+1,a_col)
#             check(t_row,t_col,a_row,a_col+1)
        
#         def look(t_row,t_col):
#             for a_row in range(self.max_row):
#                 for a_col in range(self.max_col):
#                     if mat[a_row][a_col] == 1:
#                         check(t_row,t_col,a_row,a_col)
        
#         # decide what to look for
#         for row in range(self.max_row):
#             for col in range(self.max_col):
#                 look(row,col)
        
#         return self.counter


# 長方形の左上の点を全通り試す。下方向に累積和を持っておいて、長方形の幅をインクリメントして[$ O(mn^2)]。

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        
        for j in range(n):
            for i in range(m - 2, -1, -1):
                if mat[i][j] == 1:
                    mat[i][j] += mat[i + 1][j]
        
        res = 0
        for i, j in product(range(m), range(n)):
            nj = j
            depth = mat[i][j]
            while nj < n:
                depth = min(depth, mat[i][nj])
                res += depth
                nj += 1
        
        return res  
    
    
    
    
# this is the most updated solution I have so far

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        for m in range(row):
            longest_streak = 0
            for n in range(col-1,-1,-1):
                if mat[m][n]==1:
                    longest_streak+=1
                else:
                    longest_streak=0
                mat[m][n]=longest_streak
                
        # print(mat)
        counter = 0
        # set the top left corner
        for m in range(row):
            for n in range(col):
                shortest_streak = mat[m][n]
                # set the bottom row - always get the min and add it to the count
                for i in range(m,row):
                    shortest_streak = min(shortest_streak,mat[i][n])
                    counter += shortest_streak 
        return counter 