# 222. Count Complete Tree Nodes
# Medium

# 2425

# 228

# Add to List

# Share
# Given a complete binary tree, count the number of nodes.

# Note:

# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Example:

# Input: 
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6

# Output: 6


# This solution works but not optimal:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def helper(cur):
            if not cur:
                return 0
            return 1 + helper(cur.left) + helper(cur.right)
        return helper(root)
    
    
    

# This solution works !!!
'''
# Time: O( (logN)^2 )
# Space: O( 1 )
idea: 
1) go the left most to get the level
2) then binary search for the right by doing bitwise operation and then calculate at the end
since its complete tree number of nodes is 2^level - 1

left is 0 
right is 1
00 01 10 11 

levels = how many bits there are
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        levels = 0
        cur = root
        while cur.left is not None:
            levels += 1
            cur = cur.left
        left = 0
        right = (1 << levels) - 1
        while left < right:
            mid = (left + right + 1) // 2
            cur = root
            for i in range(levels-1, -1, -1):
                if mid & (1 << i):
                    cur = cur.right
                else:
                    cur = cur.left
            if cur is None:
                right = mid - 1
            else:
                left = mid
        return (1 << levels) - 1 + left + 1