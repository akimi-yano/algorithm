# 1536. Minimum Swaps to Arrange a Binary Grid

# Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

# A grid is said to be valid if all the cells above the main diagonal are zeros.

# Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

# The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).


# Example 1:


# Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
# Output: 3
# Example 2:


# Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# Output: -1
# Explanation: All rows are similar, swaps have no effect on the grid.
# Example 3:


# Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
# Output: 0


# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 200
# grid[i][j] is 0 or 1


# this way does not work - see below
# class Solution:
    # def minSwaps(self, grid: List[List[int]]) -> int:
    #     '''
    #     3*3
        
    #     100 
    #     110
    #     111
    #     # if row<col -> have to be 0
    #     (0,0)(0,1)(0,2) 
    #     (1,0)(1,1)(1,2)
    #     (2,0)(2,1)(2,2)
    #     '''
    #     def is_valid(grid):
    #         for row in range(len(grid)):
    #             for col in range(len(grid[row])):
    #                 if row<col and grid[row][col]!=0:
    #                     return False
    #         return True
    #     k=len(grid)
    #     r=0
    #     while k>0 and not is_valid(grid) and 0<=r<=len(grid)-1:
    #         grid[r],grid[len(grid)-1-r]=grid[len(grid)-1-r],grid[r]
    #         r+=1    
    #         k-=r
    #     if is_valid(grid):
    #         return len(grid)-k
    #     else:
    #         return -1
        

# this way works ! most intuitive 

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        '''
        1 find out how many consecutive zeros (starting from the right) are in each row,
          and store that into a list. 
        2 for each element in this list, check if it satisfies the number of zeros you need for that row.
          if yes, then continue to the next row. if no, then find the first element after the current one has
          enough zeros. If there are none, it's not possible - return -1.
        3 once you find an element that has the required number of zeros, then "swap" it with
          the current row. Once swapped, move to the next row and start over.
        '''
        num_zeros = []
        for row in range(len(grid)):
            count = 0
            for col in range(len(grid[row])-1,-1,-1):
                if grid[row][col]==0:
                    count+=1
                else:
                    break
            num_zeros.append(count)
        swap=0
        for i in range(len(num_zeros)):
            if num_zeros[i]>=len(grid)-1-i:
                continue
            k=i+1
            while k<len(num_zeros) and num_zeros[k]<len(grid)-1-i:
                k+=1
            if k>=len(num_zeros):
                return -1
            num_zeros = num_zeros[:i] + [num_zeros[k]] + num_zeros[i:k] + num_zeros[k+1:]
            swap+=(k-i)
        return swap
            
                
        