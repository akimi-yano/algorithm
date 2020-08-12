# Pascal's Triangle II

# Solution
# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 3
# Output: [1,3,3,1]
# Follow up:

# Could you optimize your algorithm to use only O(k) extra space?


# this works - but lets see if we can optimize it

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [[1]]
        for i in range(1,rowIndex+1): 
            temp = []
            temp.append(1)
            for k in range(1,len(arr[-1])):    
                temp.append(arr[-1][k-1]+arr[-1][k])
            temp.append(1)
            arr.append(temp)
        return arr[rowIndex]
        
    '''
    idx 0:     1
    idx 1:    1 1
    idx 2:   1 2 1
    idx 3:  1 3 3 1 
    idx 4: 1 4 6 4 1
    
    '''
    
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row
    
'''
EXPLANATION:

say we get row = [1, 2, 1] from last iteration.
[0]+row gives us [0, 1, 2, 1] (appending 0 to the head); row+[0] gives us [1, 2, 1, 0].
Then we need to do the element-wise addition of the 2 lists.
zip() would give us element-wise zipped tuples: [(0, 1), (1, 2), (2, 1), (1, 0)], which is a iterator actually.
then we use the list comprehension to do the actual addition.
'''