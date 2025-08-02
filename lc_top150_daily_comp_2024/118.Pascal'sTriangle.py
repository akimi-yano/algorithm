'''
118. Pascal's Triangle
Solved
Easy
Topics
premium lock icon
Companies
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:



Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for _ in range(numRows-1):
            temp = []
            temp.append(1)
            for i in range(len(ans[-1])-1):
                temp.append( ans[-1][i] + ans[-1][i+1] )
            temp.append(1)
            ans.append(temp)
        return ans