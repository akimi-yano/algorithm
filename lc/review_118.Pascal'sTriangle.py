# 118. Pascal's Triangle
# Easy

# 6704

# 228

# Add to List

# Share
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30


# This solution works:


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ROW = numRows
        ans = [[1]]
        for row in range(1, ROW):
            temp = []
            temp.append(1)
            for col in range(row-1):
                new_val = ans[row-1][col]+ans[row-1][col+1]
                temp.append(new_val)
            temp.append(1)
            ans.append(temp)
        return ans