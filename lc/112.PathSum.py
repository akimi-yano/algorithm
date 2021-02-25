# 112. Path Sum
# Easy

# 2849

# 583

# Add to List

# Share
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Example 2:


# Input: root = [1,2,3], targetSum = 5
# Output: false
# Example 3:

# Input: root = [1,2], targetSum = 0
# Output: false


# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000



# This solution works!:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def helper(cur, total):
            nonlocal targetSum
            total += cur.val
            if not cur.left and not cur.right:
                return targetSum == total
            if cur.left and helper(cur.left, total):
                return True
            if cur.right and helper(cur.right, total):
                return True
            return False
        
        if not root:
            return False
        return helper(root, 0)
            



# This solution also works!:

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    # 1:27
    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True
        
        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)