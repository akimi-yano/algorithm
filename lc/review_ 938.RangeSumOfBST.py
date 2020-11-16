# 938. Range Sum of BST
# Easy

# 1742

# 262

# Add to List

# Share
# Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].


# Example 1:


# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Example 2:


# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23


# Constraints:

# The number of nodes in the tree is in the range [1, 2 * 104].
# 1 <= Node.val <= 105
# 1 <= low <= high <= 105
# All Node.val are unique.



# This solution works !

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.LO = low
        self.HI = high
        def helper(cur):
            val = 0 
            if not cur:
                return val
            
            if self.LO <= cur.val <= self.HI:
                val = cur.val

            return val + helper(cur.left) + helper(cur.right)
        
        return helper(root)
    
# This solution works !: optimization - you don't need to go left if your value already smaller than the lower bound, 
# same for right with upper bound

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.LO = low
        self.HI = high
        def helper(cur):
            val = 0 
            if not cur:
                return val
            
            if self.LO <= cur.val <= self.HI:
                val = cur.val
                return val + helper(cur.left) + helper(cur.right)
            elif self.LO > cur.val:
                return val + helper(cur.right)
            else:
                return val + helper(cur.left) 
        
        return helper(root)