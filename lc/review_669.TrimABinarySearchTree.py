# 669. Trim a Binary Search Tree
# Medium

# 3607

# 220

# Add to List

# Share
# Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

# Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

 

# Example 1:


# Input: root = [1,0,2], low = 1, high = 2
# Output: [1,null,2]
# Example 2:


# Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
# Output: [3,2,null,1]
 

# Constraints:

# The number of nodes in the tree in the range [1, 104].
# 0 <= Node.val <= 104
# The value of each node in the tree is unique.
# root is guaranteed to be a valid binary search tree.
# 0 <= low <= high <= 104


# This solution works:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def helper(cur):
            if not cur:
                return
            if low>cur.val:
                return helper(cur.right)
            if cur.val>high:
                return helper(cur.left)
            cur.left = helper(cur.left)
            cur.right = helper(cur.right)
            return cur
        return helper(root)