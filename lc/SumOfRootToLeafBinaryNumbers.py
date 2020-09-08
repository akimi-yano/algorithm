# Sum of Root To Leaf Binary Numbers

# Input: [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


#    1
#    /\
#  0   1
# /\   /\
# 0 1 0 1

# 100 101 110 111


#    1           [1 + prev for prev in prevs]
#    /\
#  0   1
# /\   /\         r[[0 + prev1 , 0+prev2]  +  [1 + prev1 , 0+prev2] ] - extend
# 0 1 0 1    -    r[0] r [1] - base case   r[0] r [1] - base case   



# THIS SOLUTION WORKS !!! - I feel like there are better ways to do this, but I'm happy I did it myself.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        '''
        1 make an array of string
        2 traverse the array to make an int and sum
        '''
        def helper(cur):
            if not cur:
                return []
            if not cur.left and not cur.right:
                return [[cur.val]]
            arr = []
            arr += helper(cur.left)
            arr  += helper(cur.right)
            arr =[[cur.val] + temp for temp in arr]
            return arr
        options = helper(root)
        # print(options)
        return sum([int("".join([str(c) for c in num]),2) for num in options])
        