# 637. Average of Levels in Binary Tree
# Easy

# 1831

# 194

# Add to List

# Share
# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Note:
# The range of node's value is in the range of 32-bit signed integer.

# This solution works:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return 0
        queue = deque([root])
        ans = []
        while queue:
            newqueue = deque([])
            total = 0
            count = 0
            while queue:
                node = queue.popleft()
                total += node.val
                count += 1
                if node.left:
                    newqueue.append(node.left)
                if node.right:
                    newqueue.append(node.right)
            ans.append(total/count)
            queue = newqueue
        return ans
        