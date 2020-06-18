# 1260. Shift 2D Grid


# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

# In one shift operation:

# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.

 

# Example 1:


# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[9,1,2],[3,4,5],[6,7,8]]
# Example 2:


# Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
# Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
# Example 3:

# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
# Output: [[1,2,3],[4,5,6],[7,8,9]]
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m <= 50
# 1 <= n <= 50
# -1000 <= grid[i][j] <= 1000
# 0 <= k <= 100

# class Solution:
#     def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # max_row = len(grid)-1
        # max_col =len(grid[0])-1
        # for row in range(max_row,-1,-1):
        #     for col in range(max_col,-1,-1):
        #         if row == max_row and col == max_col:
        #             grid[row][col],grid[0][0]= grid[0][0],grid[row][col]
        #         elif col == max_col:
        #             grid[row][col],grid[row+1][0]= grid[row+1][0],grid[row][col]
        #         else:
        #             if not (row==0 and col ==0):
        #                 grid[row][col],grid[row][col+1]= grid[row][col+1],grid[row][col]
        # return grid
        # for i in range(0,(len(grid)*len(grid[0])),-1):
        # start with len(grid)-1-k
        
        # k == 0:
        #     start = [0][0]
        # or 
        #     start = [len(grid)-1 -2][len(grid)-1 -2]
        # k == 1:
        #     start = [len(grid)-1][len(grid)[0]-1]
        # k == 2:
        #     start = [len(grid)-1][len(grid)[0]-1 -1]
        # k == 3:
        #     start = [len(grid)-1][len(grid)[0]-1 -2]
        # k == 4:
        #     start = [len(grid)-1 -1][len(grid)[0]-1]
        # k == 5:
        #     start = [len(grid)-1 -1][len(grid)[0]-1 -1]
        # k == 6:
        #     start = [len(grid)-1 -1][len(grid)[0]-1 -2]
        # k == 7:
        #     start = [len(grid)-1 -2][len(grid)[0]-1]
        # k == 8:
        #     start = [len(grid)-1 -2][len(grid)[0]-1 -1]
        # k == 9:
#         #     start = [len(grid)-1 -2][len(grid)[0]-1 -2]
#         if k==0:
#             return grid
#         ans = []
#         max_row = len(grid)-1
#         max_col = len(grid[0])-1
      
#         k=k%(len(grid)*len(grid[0])-1)
#         start_row = max_row//k
#         start_col = max_col//k
        
#         # print("m",m,"n",n,"k",k)
#         # print("m",m//k)
#         # print("n",n//k)
# #         for row in range(len(grid)-1-k+1,-1,-1):
# #             temp = []
# #             for col in range(len(grid[row])-1-k+1,len(grid[row]),1):
# #                 temp.append(grid[row][col])
# #             ans.append(temp)
# #         return ans 
#         for row in range(start_row,max_row+1):
#             temp = []
#             for col in range(start_col,max_col+1):
#                 temp.append(grid[row][col])
#             ans.append(temp)
#         return ans
        
        
        
        
# why did i know figure out ?

# new_row = (row+(col+k)//col_len)%row_len
# new_col = (col+k)%col_len

# maybe :
    # i was focused too much on manipulating range for iteration
    # I could not break down the problem small enough 
    # col+k

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ans =[]
        for row in range(len(grid)):
            ans.append([])
            for col in range(len(grid[row])):
                ans[row].append(None)

        row_len = len(grid)
        col_len = len(grid[0])
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                new_row = (row+(col+k)//col_len)%row_len
                new_col = (col+k)%col_len
                ans[new_row][new_col] = grid[row][col]
        return ans
    
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ans =[]
        row_len = len(grid)
        col_len = len(grid[0])
        for row in range(row_len):
            ans.append([])
            for col in range(col_len):
                old_row = (row+(col-k)//col_len)%row_len
                old_col = (col-k)%col_len
                ans[row].append(grid[old_row][old_col])
        return ans