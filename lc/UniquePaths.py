# latice path unique path problems are different problems !


# difference :
# lattice path - counting the edges  
# robot unique path - counting the boxes (so -1)



# also for lattice path,

# instead of doing this ----


#     if m == 0 and n == 0:
#         return 1
#     elif m<0 or n<0:
#         return 0

# you can just do this --- which is more efficient

    # if m == 0 or n == 0:
    #     return 1





# 1. Lattice Paths
#
# Prompt:  Count the number of unique paths to travel from the top left
#          corder to the bottom right corner of a lattice of M x N squares.
#
#          When moving through the lattice, one can only travel to the
#          adjacent corner on the right or down.
#
# Input:   m {Integer} - rows of squares
# Input:   n {Integer} - column of squares
# Output:  {Integer}
#
# Example: input: (2, 3)
#
#          (2 x 3 lattice of squares)
#           __ __ __
#          |__|__|__|
#          |__|__|__|
#
#          output: 10 (number of unique paths from top left corner to bottom right)
#
# Resource: https://projecteuler.net/problem=15


# def latticePaths(m, n):
#     if m == 0 and n == 0:
#         return 1
#     elif m<0 or n<0:
#         return 0
#     return latticePaths(m-1, n) + latticePaths(m,n-1)
#     # Write your code here
# print(latticePaths(2,2))
# print(latticePaths(2,3))

def latticePaths(m, n):
    if m == 0 or n == 0:
        return 1

    return latticePaths(m-1, n) + latticePaths(m,n-1)
    # Write your code here
print(latticePaths(2,2))
print(latticePaths(2,3))



# 2.Unique Paths

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach 
# the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?
# Above is a 7 x 3 grid. How many possible unique paths are there?

# Example 1:
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right

class Solution:
    def __init__(self):
        self.memo = {}
        
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1:
            return 1
        if (m, n) not in self.memo:
            self.memo[(m, n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return self.memo[(m, n)]
    
        