# 1302. Deepest Leaves Sum
# Medium

# 1223

# 56

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
    def deepestLeavesSum(self, root: TreeNode) -> int:

        def helper(cur, level):
            nonlocal deepest_level, deepest_total
            if not cur.left and not cur.right:
                if level == deepest_level:
                    deepest_total += cur.val
                elif level > deepest_level:
                    deepest_level = level
                    deepest_total = cur.val
                return
            if cur.left:
                helper(cur.left, level+1)
            if cur.right:
                helper(cur.right, level+1)
        
        deepest_level = 0
        deepest_total = 0                        
        helper(root, 0)
        return deepest_total