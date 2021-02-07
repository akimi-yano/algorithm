# 199. Binary Tree Right Side View
# Medium

# 3449

# 183

# Add to List

# Share
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example:

# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# This solution works !!!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            ans.append(queue[-1].val)
            newqueue = deque([])
            while queue:
                cur = queue.popleft()
                if cur.left:
                    newqueue.append(cur.left)
                if cur.right:
                    newqueue.append(cur.right)
            queue = newqueue
        return ans
        