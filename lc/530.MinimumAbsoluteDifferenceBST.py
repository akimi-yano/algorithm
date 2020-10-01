# 530. Minimum Absolute Difference in BST
# Easy

# 965

# 71

# Add to List

# Share
# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

# Example:

# Input:

#    1
#     \
#      3
#     /
#    2

# Output:
# 1

# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 

# Note:

# There are at least two nodes in this BST.
# This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/



# This solution works !
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def helper(cur, arr):
            if not cur:
                return []
            helper(cur.left, arr)
            arr.append(cur.val)
            helper(cur.right, arr)
            return arr
        
        inorder = helper(root, [])
        min_diff = float('inf')
        prev = float('inf')
        for elem in inorder:
            min_diff = min(min_diff, abs(elem-prev))
            prev = elem
        return min_diff
    
    

# This solution works and more concise :

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.best = float('inf')

        def helper(cur, prev):
            if not cur:
                return prev
            new_prev = helper(cur.left, prev)
            
            self.best = min(self.best, cur.val - new_prev)
            
            new_prev = helper(cur.right, cur.val)
            
            return new_prev

        helper(root, float('-inf'))
        return self.best