# 120. Triangle
# Medium

# 2812

# 311

# Add to List

# Share
# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

# Example 1:

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:

# Input: triangle = [[-10]]
# Output: -10
 

# Constraints:

# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104
 

# Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?


# This solution works:

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache(None)
        def helper(row, col):
            num_col = row + 1
            if col >= num_col:
                return float('inf')
            if row > len(triangle)-1:
                return 0
            return triangle[row][col] + min(helper(row+1, col), helper(row+1, col+1))
        return helper(0, 0)

    
# This solution works:

class Solution:
    def minimumTotal(self, T: List[List[int]]) -> int:
        '''
        from the bottom and right to the up and left
        from 2nd to last one
        look at the previous row and update the one you are looking at
        return the one at the top as it is guaranteed that the top one exists!
        '''
        for i in range(len(T)-2,-1,-1):
            for j in range(len(T[i])-1,-1,-1):
                T[i][j] += min(T[i+1][j], T[i+1][j+1])
        return T[0][0]