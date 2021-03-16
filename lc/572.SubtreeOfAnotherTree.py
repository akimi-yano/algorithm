# 572. Subtree of Another Tree
# Easy

# 3216

# 160

# Add to List

# Share
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

# Example 1:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4 
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
 

# Example 2:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.


# This solution works:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t or not s:
            return False
        
        def helper(cur):
            if not cur:
                return
            if cur.val == target_val:
                roots.append(cur)
            helper(cur.left)
            helper(cur.right)
            
        roots = []
        target_val = t.val
        helper(s)
        
        def helper2(cur1, cur2):
            if not cur1 or not cur2:
                return not cur1 and not cur2
    
            if cur1.val == cur2.val and helper2(cur1.left, cur2.left) and helper2(cur1.right, cur2.right):
                return True
            return False
        
        for root in roots:
            if helper2(root, t):
                return True
        return False