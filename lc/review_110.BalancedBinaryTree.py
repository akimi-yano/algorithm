# 110. Balanced Binary Tree
# Easy

# 2951

# 200

# Add to List

# Share
# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104


# This solution works !

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(cur):
            if not cur:
                return 0, True
            left, left_balanced = helper(cur.left)
            right, right_balanced = helper(cur.right)
            is_balanced = True
            if left == right:
                pass
            elif left > right and left == right+1:
                pass
            elif left < right and left +1 == right:
                pass
            else:
                is_balanced = False
            
            return max(left, right) + 1, is_balanced & left_balanced & right_balanced
        return helper(root)[1]