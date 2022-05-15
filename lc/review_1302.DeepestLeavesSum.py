# 1302. Deepest Leaves Sum
# Medium

# 2568

# 78

# Add to List

# Share
# Given the root of a binary tree, return the sum of values of its deepest leaves.
 

# Example 1:


# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# Example 2:

# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 100


# This solution works:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def helper(cur, depth):
            nonlocal total, max_depth
            if not cur:
                return
            if depth > max_depth:
                max_depth = depth
                total = cur.val
            elif depth == max_depth:
                total += cur.val
            
            helper(cur.left, depth+1)
            helper(cur.right, depth+1)
        
        total = 0
        max_depth = 0
        helper(root, 0)
        return total