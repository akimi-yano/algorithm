# 1026. Maximum Difference Between Node and Ancestor
# Medium

# 1646

# 47

# Add to List

# Share
# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

 

# Example 1:


# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
# Example 2:


# Input: root = [1,null,2,null,0,3]
# Output: 3
 

# Constraints:

# The number of nodes in the tree is in the range [2, 5000].
# 0 <= Node.val <= 105


# This solution works:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(cur, MAX, MIN):
            nonlocal largest_diff
            largest_diff = max(largest_diff, abs(MAX-MIN))
            if cur.left:
                helper(cur.left, max(MAX, cur.left.val), min(MIN, cur.left.val))
            if cur.right:
                helper(cur.right, max(MAX, cur.right.val), min(MIN, cur.right.val))
        largest_diff = 0
        helper(root, root.val, root.val)
        return largest_diff
        